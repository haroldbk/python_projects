#https://www.youtube.com/watch?v=M7UdAX77kpY
import sys 
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtMultimedia as qtmm

class PlayButton(qtw.QPushButton):
    play_stylesheet = 'background-color: lightgreen; color:black;'
    stop_stylesheet ='background-color: darkred, color:white;'
    def __init__(self):
        super().__init__('Play')
        self.setFont(qtg.QFont('Sans', 32, qtg.QFont.Bold))
        self.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding
        )
        self.setStyleSheet(self.play_stylesheet)
    def on_state_changed(self, state):
        if state == qtmm.QMediaPlayer.PlayingState:
            self.setStyleSheet(self.stop_stylesheet)
            self.setText('Stop')
        else:
            self.setStyleSheet(self.play_stylesheet)
            self.setText("Play")    

class RecordButton (qtw.QPushButton):
    record_stylesheet = 'background-color:black; color: white;'
    stop_stylesheet= 'background-color: darkred; color:white;'

    def __init__(self):
        super().__init__('Record')
    def on_state_changed(self, state) :
        if state == qtmm.QAudioRecorder.RecordingState:
            self.setStyleSheet(self.stop_stylesheet)
            self.setText('Stop')  
        else:
            self.setStyleSheet(self.record_stylesheet)
            self.setText('Record')

class SoundWidget(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QGridLayout())
        self.label=qtw.QLabel('No file loaded')
        self.layout().addWidget(self.label,0,0,1,2)
        self.play_button = PlayButton()
        self.layout().addWidget(self.play_button,3,0,1,2)
        self.player = qtmm.QMediaPlayer()
        self.play_button.clicked.connect(self.on_playbutton)
        self.player.stateChanged.connect(self.play_button.on_state_changed)

        #loading files
        self.file_button = qtw.QPushButton(
            'load file',
            clicked=self.get_file)
        self.layout().addWidget(self.file_button,4,0)
        
        # slider
        self.position = qtw.QSlider(
            minimum =0, orientation=qtc.Qt.Horizontal)
        self.layout().addWidget(self.position,1,0,1,2)

        self.player.positionChanged.connect(self.position.setSliderPosition)
        self.player.durationChanged.connect(self.position.setMaximum)
        self.position.sliderMoved.connect(self.player.setPosition)

        # looping
        self.loop_cb=qtw.QCheckBox(
            'Loop', stateChanged=self.on_loop_cb
        )
        self.layout().addWidget(self.loop_cb, 2,0)

        # volume
        self.volume = qtw.QSlider(
            minimum=0,
            maximum=100,
            sliderPosition=75,
            orientation=qtc.Qt.Horizontal,
            sliderMoved=self.player.setVolume
        )

        self.layout().addWidget(self.volume,2,1)

        # recording
        self.recorder = qtmm.QAudioRecorder()

        self.record_button = RecordButton()
        self.recorder.stateChanged.connect(self.record_button.on_state_changed)
        self.layout().addWidget(self.record_button,4,1)

        self.record_button.clicked.connect(self.on_recordbutton)



   ## functions ##     
    def get_file(self):
        fn, _ = qtw.QFileDialog.getOpenFileUrl(
            self,
            'Select File', 
            qtc.QUrl.fromLocalFile(qtc.QDir.homePath()),
            'Audio file (*.wav *.flac *.mp3);;All files(*)'
        )
        if fn:
            self.set_file(fn)
    def set_file(self,url):
        self.label.setText(url.fileName()) 
        if url.scheme()=='':
            url.setScheme('file')
        content = qtmm.QMediaContent(url)
        #self.player.setMedia(content)
        self.playlist=qtmm.QMediaPlaylist()
        self.playlist.addMedia(content)
        self.playlist.setCurrentIndex(1)
        self.player.setPlaylist(self.playlist)
        self.loop_cb.setChecked(False)


    def on_playbutton(self):
        if self.player.state() == qtmm.QMediaPlayer.PlayingState:
            self.player.stop()
        else:
            self.player.play()    

    def on_loop_cb(self, state):
        if state==qtc.Qt.Checked:
            self.playlist.setPlaybackMode(qtmm.QMediaPlaylist.CurrentItemInLoop)
        else:
            self.playlist.setPlaybackMode(qtmm.QMediaPlaylist.CurrentItemOnce)  

    def on_recordbutton(self):
        if self.recorder.state()==qtmm.QMediaRecorder.RecordingState:
            self.recorder.stop()
            url = self.recorder.actualLocation()
            self.set_file(url)
        else:
            self.recorder.record()                

class MainWindow(qtw.QMainWindow):  
   
    def __init__(self):
        super().__init__()
       
        #your code here
        rows=3
        columns =3
        soundboard=qtw.QWidget()
        soundboard.setLayout(qtw.QGridLayout())
        self.setCentralWidget(soundboard)
        for c in range(columns):
            for r in range(rows):
                sw=SoundWidget()
                soundboard.layout().addWidget(sw,c,r)


        #your code ends here
        self.show()     


if __name__=='__main__':
    app =qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())


