#https://www.youtube.com/watch?v=M7UdAX77kpY
import sys 
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtMultimedia as qtmm
import resources 



class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
       
        #your code here
        self.button = qtw.QPushButton('1')
        self.setCentralWidget(self.button)
        self.button.clicked.connect(self.playSound)
       
        self.sound = qtmm.QSoundEffect()
        #your code ends here
        self.show()  

    def playSound(self):          
           self.sound.setSource(qtc.QUrl('qrc:/dtmf/8.wav'))
           self.sound.setLoopCount(1)
           self.sound.setVolume(0.5)
           self.sound.play() 
            


if __name__=='__main__':
    app =qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())


