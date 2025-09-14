#https://www.youtube.com/watch?v=M7UdAX77kpY
import sys 
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtMultimedia as qtmm
import resources

class SoundButton(qtw.QPushButton):
    def __init__(self,wav_file,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.wave_file = wav_file
        self.player = qtmm.QSoundEffect()
        self.player.setSource(qtc.QUrl(f'qrc:/dtmf/{wav_file}'))
        self.clicked.connect(self.player.play)



class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
       
        #your code here
        dialpad = qtw.QWidget()
        self.setCentralWidget(dialpad)
        dialpad.setLayout(qtw.QGridLayout())
        
        for i, symbol in enumerate('123456789*0#'):
            button = SoundButton(f'{symbol}.wav',symbol)
            row = i//3
            column = i % 3
            dialpad.layout().addWidget(button, row, column)
        #your code ends here
        self.show()     


if __name__=='__main__':
    app =qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())


