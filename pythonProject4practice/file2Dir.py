import os
import sys
from pathlib import Path
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QDialog


# SUBDIR = {
#     "DOCUMENTS": [".pdf", ".docx", ".txt", ".html",".doc"],
#     "AUDIO": [".m4a", ".m4b", ".mp3", ".mp4"],
#     "IMAGES": [".jpg", ".jpeg", ".png", ".gif"],
#     "DataFile": [".csv", ".xlsx",".xls"]
# }

class MyFirstWin(QDialog):
    def __init__(self):
        super(MyFirstWin,self).__init__()
        uic.loadUi('myfirstwin.ui',self)

        self.zlButton.clicked.connect(self.onClick1)
        self.tcButton.clicked.connect(self.onClick2)

    def onClick1(self):
        self.text1.setText('Hello World!')

    def onClick2(self):
        self.text1.clear()


def show_MyFirstWin():
    app = QtWidgets.QApplication(sys.argv)
    myFirstWin = MyFirstWin()
    myFirstWin.show()
    sys.exit(app.exec())



if __name__ == '__main__':
    show_MyFirstWin()
