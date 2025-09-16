#https://www.youtube.com/watch?v=M7UdAX77kpY
import sys 
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtNetwork as qtn

class ChatWindow(qtw.QWidget):
    submitted = qtc.pyqtSignal(str)
    def __init__(self):
        super().__init__() 
        self.setLayout(qtw.QGridLayout())
        self.message_view = qtw.QTextEdit(readOnly=True)
        self.layout().addWidget(self.message_view,1,1,1,2)
        self.message_entry = qtw.QLineEdit()
        self.layout().addWidget(self.message_entry, 2,1)
        self.send_btn=qtw.QPushButton('Send',clicked=self.send)
        self.layout().addWidget(self.send_btn,2,2)

    def write_message(self,username,message):
        self.message_view.append(f'<b> {username}: </b>{message}<br>')
    def send(self):
        message = self.message_entry.text().strip()
        if message:
            self.submitted.emit(message)
            self.message_entry.clear()

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
       
        #your code here
        self.cw = ChatWindow()
        self.setCentralWidget(self.cw)

        #your code ends here
        self.show()     
        


if __name__=='__main__':
    app =qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())



