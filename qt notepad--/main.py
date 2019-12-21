import PyQt5, sys, os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog

try:
    os.system("cls")
except:
    pass

class window():
    app, win = "", ""

    def save_file(self):
        fname = QFileDialog.getSaveFileName()

        if fname[0]:
            f = open(fname[0], 'w+')
            text = self.win.textArea.toPlainText()
            f.write(text)
            f.close()

    def load_file(self):
        fname = QFileDialog.getOpenFileName()
        
        if fname[0]:
            f = open(fname[0], 'r')
            
            with f:
                data = f.read()
                self.win.textArea.setText(data)
            self.win.fileLabel.setText(fname[0])

    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.win = uic.loadUi("layout.ui")
        self.win.fileLabel.setText("")

        self.win.loadButton.clicked.connect(self.load_file)
        self.win.saveButton.clicked.connect(self.save_file)
        self.win.setMinimumSize(810,515)
        self.win.setMaximumSize(810,515)

        self.win.show()
        self.app.exec_()

win = window()