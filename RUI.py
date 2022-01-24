
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(354, 459)
        MainWindow.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(250, 40, 91, 31))
        self.SubmitButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"border-radius: 15px;\n"
"}")
        self.SubmitButton.setObjectName("SubmitButton")
        self.inputBar = QtWidgets.QLineEdit(self.centralwidget)
        self.inputBar.setGeometry(QtCore.QRect(20, 40, 221, 31))
        self.inputBar.setStyleSheet("background-color: rgb(152, 152, 227);\n"
"border-radius: 15px;\n"
"padding:10px;\n"
"")
        self.inputBar.setObjectName("inputBar")
        self.listwindow = QtWidgets.QListView(self.centralwidget)
        self.listwindow.setGeometry(QtCore.QRect(20, 90, 311, 341))
        self.listwindow.setMouseTracking(False)
        self.listwindow.setAutoFillBackground(True)
        self.listwindow.setStyleSheet("border:0px;")
        self.listwindow.setObjectName("listwindow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        

    def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.SubmitButton.setText(_translate("MainWindow", "Search"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

