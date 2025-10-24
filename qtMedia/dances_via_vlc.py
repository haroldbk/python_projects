from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys
import os 
import SQLite3_get_dances as sq

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

        self.video_frame = qtw.QFrame()
        left_layout.addWidget(self.video_frame)

        # Playback controls
        controls = qtw.QHBoxLayout()
        self.play_button = qtw.QPushButton("Play")
        self.pause_button = qtw.QPushButton("Pause")
        self.stop_button = qtw.QPushButton("Stop")
        controls.addWidget(self.play_button)
        controls.addWidget(self.pause_button)
        controls.addWidget(self.stop_button)
        self.speed_label = qtw.QLabel("Speed: 1.0x")
        self.speed_slider = qtw.QSlider(qtc.Qt.Horizontal)
        self.speed_slider.setMinimum(5)  # Represents 0.5x
        self.speed_slider.setMaximum(20) # Represents 2.0x
        self.speed_slider.setValue(10)  # Defaults 1.0x
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
        self.folder_list.currentIndexChanged.connect(self.on_item_clicked)
        self.file_list.itemClicked.connect(self.on_file_clicked)

        # Add tabs to splitter
        splitter.addWidget(left_tab)
        splitter.addWidget(right_tab)
        self.setCentralWidget(splitter)

        


    def setup_vlc(self):
        import vlc
        self.instance = vlc.Instance()        
        self.player = self.instance.media_player_new()
        win_id = int(self.video_frame.winId())
        self.player.set_hwnd(win_id)

        # ✅ Now that self.player exists, wire up buttons
        self.play_button.clicked.connect(self.player.play)
        self.pause_button.clicked.connect(self.player.pause)
        self.stop_button.clicked.connect(self.player.stop)


    def populate_list(self):
        dances=[]
        self.folder_list.clear()
        dance_names = sq.getName()
        for dance in dance_names:
            dances.append(dance[1])
          
        self.folder_list.addItems(dances)
             #fldrlst=['mixed','shag','Hustle_with_Beatta','temp_videos']            
             #self.folder_list.addItems(fldrlst)
    def populate_video_list(self,item):
         folder_name = item.text()
         folder_path = os.path.join()       

    def on_item_clicked(self, item):
        folder_name = self.folder_list.itemText(item)
        folder_path = os.path.join(r"D:\odLive\OneDrive\Dance_demos", folder_name)
        print('file path', folder_path)
        self.file_list.clear()
        videos=[]
        
        if folder_name:
         dance = folder_name     
         #qtw.QMessageBox.information(None, "Selected file", dance)   
         dance_videos= sq.getDances(dance) 
         for dn in dance_videos:
             videos.append(dn[2])
        #for file in os.listdir(folder_path):
         #              if file.lower().endswith(('.mp4','.mov','.mkv')):
         #     self.file_list.addItem(file)
        self.file_list.addItems(videos)
        self.current_folder = folder_path     

    def on_file_clicked(self,item):  
         print("item", item)
         file_path = os.path.join(self.current_folder,item.text())
         media = self.instance.media_new(file_path)
         self.player.set_media(media)
         self.player.play()

    def update_speed(self, value):
        rate = value/10.0
        self.player.set_rate(rate)
        self.speed_label.setText(f'Speed: {rate:.1f}x')

    def reset(self):
        self.speed_slider.setValue(10)    

          
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
