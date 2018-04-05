import sys
from JSON_call import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class TestQt(QDialog):
    def __init__(self):
        super(TestQt, self).__init__()
        loadUi('testQt.ui', self)
        self.setWindowTitle('Yo GUI')
        self.serverIDI.setText('10.2.68.211')
        self.taskIDI.setText('77')
        # self.serverIDI.setText('172.18.34.241')
        # self.taskIDI.setText('23')
        self.taskIDI.setValidator(QIntValidator())
        # self.serverIDI.textChanged.connect(self.textchanged)
        self.runButton.clicked.connect(self.on_runButton_clicked)
        self.convertButton.clicked.connect(self.on_convertButton_clicked)
        self.searchTaskTimeCost = 0
        self.searchTaskTimeCost_min = 0
        self.searchTaskTimeCost_second = 0
        self.searchTaskTimeUnit = 's'
        self.serverID = ''
        self.taskID = ''
        self.displayL.setText('Will changed here ... ')

    # @pyqtSlot()
    def on_runButton_clicked(self):
        self.serverID = self.serverIDI.text()
        self.taskID = self.taskIDI.text()
        s = Session(self.serverID, 'admin', '')
        taskTimeCost = s.getTaskLoadingTime(int(self.taskID), 's')
        self.searchTaskTimeCost = int(float(taskTimeCost.replace('s', '')))
        self.searchTaskTimeUnit = 's'
        if (taskTimeCost != ''):
            self.displayL.setText(
                "Task ID " + self.taskID + ": Time Cost: " + str(self.searchTaskTimeCost) + self.searchTaskTimeUnit)
        else:
            self.displayL.setText("Task ID " + self.taskID + " is not exists. ")

    #
    # @pyqtSlot()
    def on_convertButton_clicked(self):
        if self.searchTaskTimeUnit == 's':
            self.searchTaskTimeCost_min = int(self.searchTaskTimeCost / 60)
            self.searchTaskTimeCost_second = self.searchTaskTimeCost % 60
            self.searchTaskTimeUnit = 'm'
            self.displayL.setText(
                "Task ID " + self.taskID + ": Time Cost: " + str(self.searchTaskTimeCost_min) + 'm' + str(
                    self.searchTaskTimeCost_second) + 's')
        else:
            self.searchTaskTimeCost = self.searchTaskTimeCost_min * 60 + self.searchTaskTimeCost_second
            self.searchTaskTimeUnit = 's'
            self.displayL.setText(
                "Task ID " + self.taskID + ": Time Cost: " + str(self.searchTaskTimeCost) + self.searchTaskTimeUnit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = TestQt()
    widget.show()
    sys.exit(app.exec_())
