from PyQt5 import QtWidgets as qtw
from PyQt5 import  QtCore as qtc
import sys
import os 
import odlive as od 
import requests

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video + Lists Layout")
        self.resize(800, 600)
        self.setup_ui() 
        self.setup_vlc()              
        self.populate_list()
        
    def setup_ui(self):
        # Create splitter
        splitter = qtw.QSplitter(qtc.Qt.Horizontal)
        splitter.setSizes([500,300])
        # Left tab: video + controls
        left_tab = qtw.QWidget()
        left_layout = qtw.QVBoxLayout(left_tab)
        video_volume_layout = qtw.QHBoxLayout()
        self.video_frame = qtw.QFrame()
        self.video_frame.setMinimumSize(400,300)

        video_volume_layout.addWidget(self.video_frame,stretch=10)
          #volume control
        self.volume_slider = qtw.QSlider(qtc.Qt.Vertical)
        self.volume_slider.setRange(0,100)
        self.volume_slider.setValue(50)
        self.volume_slider.setTickPosition(qtw.QSlider.TicksRight)
        self.volume_slider.setTickInterval(10)
        self.volume_slider.valueChanged.connect(self.set_volume)
        volume_layout=qtw.QVBoxLayout()
        volume_label = qtw.QLabel('Volume')
        volume_layout.addWidget(volume_label)
        volume_layout.addWidget(self.volume_slider)

         # wrap volume layout in a widget so it can be added to the horizontal layout
        volume_widget = qtw.QWidget()
        volume_widget.setMaximumWidth(60)
        volume_widget.setLayout(volume_layout)    
        video_volume_layout.addWidget(volume_widget, stretch=1)

        #add the combined layout to the left tab

        left_layout.addLayout(video_volume_layout)
        self.token=''  # fix here

        # Playback controls
        controls = qtw.QHBoxLayout()
        self.play_button = qtw.QPushButton("Play")
        self.pause_button = qtw.QPushButton("Pause")
        self.stop_button = qtw.QPushButton("Stop")
        controls.addWidget(self.play_button)
        controls.addWidget(self.pause_button)
        controls.addWidget(self.stop_button)
        self.speed_label = qtw.QLabel('Speed: 1.0x')
        self.speed_slider = qtw.QSlider(qtc.Qt.Horizontal)
        self.speed_slider.setMinimum(5) # represents 0.5x
        self.speed_slider.setMaximum(20) # represents 2.0x
        self.speed_slider.setValue(10) # default at 1.0x
        self.speed_slider.setTickInterval(1)
        self.speed_slider.setTickPosition(qtw.QSlider.TicksBelow)
        self.speed_slider.valueChanged.connect(self.update_speed)
        self.reset_speed = qtw.QPushButton('reset')
        self.reset_speed.clicked.connect(self.reset)
        controls.addWidget(self.speed_label)
        controls.addWidget(self.speed_slider)
        controls.addWidget(self.reset_speed)
        left_layout.addLayout(controls)

        # Right tab: file list
        right_tab = qtw.QWidget()
        right_layout = qtw.QVBoxLayout(right_tab)

        self.folder_list = qtw.QComboBox()
        self.file_list= qtw.QListWidget()
        right_layout.addWidget(qtw.QLabel("folders"))
        right_layout.addWidget(self.folder_list)
        right_layout.addWidget(qtw.QLabel("Files"))
        right_layout.addWidget(self.file_list)

        # Connect list click
        #self.folder_list.currentIndexChanged.connect(self.on_item_clicked)
        self.folder_list.currentIndexChanged.connect(self.populate_video_list)
        qtc.QTimer.singleShot(100,self.populate_video_list)
        self.file_list.itemClicked.connect(self.on_file_clicked)

        # Add tabs to splitter
        splitter.addWidget(left_tab)
        splitter.addWidget(right_tab)
        self.setCentralWidget(splitter)

        


    def setup_vlc(self):
        import vlc
        self.instance = vlc.Instance()        
        self.player = self.instance.media_player_new()
        if sys.platform.startswith('linux'):
          self.player.set_xwindow(int(self.video_frame.winId()))
        elif sys.platform.startswith('win32'):  
          self.player.set_hwnd(self.video_frame.winId())  
        elif sys.platform.startswith('darwin'): #mac
          self.player.set_nsobject(int(self.video_frame.winId())) 
        #self.player.set_hwnd(win_id)

        # ✅ Now that self.player exists, wire up buttons
        self.play_button.clicked.connect(self.player.play)
        self.pause_button.clicked.connect(self.player.pause)
        self.stop_button.clicked.connect(self.player.stop)


    def populate_list(self):
            #self.folder_list.clear()
            fldrlst=['mixed','shag','Hustle_with_Beatta']         
            self.folder_list.addItems(fldrlst)

    def populate_video_list(self):
      self.file_list.clear()
      folder = self.folder_list.currentText()
      if folder ==None:
          folder = 'mixed'
          
      access_token, filelist = od.main(folder)
      if filelist[0][0]=='error':
         msg = "Error accessing OneDrive: 404"
         print(msg)
         qtw.QMessageBox.critical(None, "error", msg)
         
      else:
       self.token = access_token
       for file in filelist:
            item= qtw.QListWidgetItem(file[1])
            item.setData(qtc.Qt.UserRole, file[0])             
            self.file_list.addItem(item)
            #print (f'item: {item}')

    def on_item_clicked(self, item):
        folder_name = self.folder_list.itemText(item)
        folder_path = os.path.join(r"D:\odLive\OneDrive\Dance_demos", folder_name)
        print('file path', folder_path)
        self.file_list.clear()
        for file in os.listdir(folder_path):
             if file.lower().endswith(('.mp4','.mov','.mkv')):
              self.file_list.addItem(file)
        self.current_folder = folder_path     

    def on_file_clicked(self,item):  
         print("item", item)
         selected_item = self.file_list.currentItem()
         file_id = selected_item.data(qtc.Qt.UserRole)
         headers =  {'Authorization': f'Bearer {self.token}'}
         resp = requests.get(f'https://graph.microsoft.com/v1.0/me/drive/items/{file_id}',
                        headers = headers)       
         url = resp.json()["@microsoft.graph.downloadUrl"]       
         media = self.instance.media_new(url)
         self.player.set_media(media)
         self.player.play()

    def update_speed(self, value):
        rate = value/10.0
        self.player.set_rate(rate)
        self.speed_label.setText(f'Speed: {rate:.1f}x')  

    def reset(self):       
        self.speed_slider.setValue(10)

    def set_volume(self,value):
        self.player.audio_set_volume(value)
   
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
