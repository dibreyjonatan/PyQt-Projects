import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from utils import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Increment Decrement")
        self.pushButton.clicked.connect(self.Inc)
        self.pushButton_2.clicked.connect(self.Dec)

        self.value=0
    def Inc(self):
        self.value+=1
        self.label.setText(str(self.value))
        
    def Dec(self):
        self.value-=1
        self.label.setText(str(self.value))


if __name__== "__main__" :
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec_()
