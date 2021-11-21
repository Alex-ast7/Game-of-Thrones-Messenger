from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase
from win32api import GetSystemMetrics


SCREEN_HEIGHT = GetSystemMetrics(1) * 0.8
SCREEN_WIDTH = GetSystemMetrics(0) * 0.25

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        fontDB = QFontDatabase()
        fontDB.addApplicationFont('data/fonts/Trajan.ttf')
        self.centralwidget.setStyleSheet('background-color: #363636')
        self.main_label = QtWidgets.QPushButton(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(0, 0, SCREEN_WIDTH,
                                                 SCREEN_HEIGHT * 0.07))
        self.main_label.setText('Game Of Thrones')
        self.main_label.setStyleSheet('font-size: 24px;'
                                      'font-family: "Trajan Pro 3";'
                                  'color: qlineargradient(spread:pad, '
                                  'x1:0, y1:0.5, x2:1, y2:0.5, stop:0 '
                                  'rgba(209, 166, 107, 255), stop:0.15 '
                                  'rgba(203, 155, 81, 255), stop:0.37 '
                                  'rgba(246, 226, 122, 255), stop:0.5 '
                                  'rgba(246, 242, 192, 255), stop:0.63 '
                                  'rgba(246, 226, 122, 255), stop:0.85 '
                                  'rgba(203, 155, 81, 255), stop:1 '
                                  'rgba(209, 166, 107, 255));'
                                 'border-style: outset;'
                                 'border-width: 0px;'
                                 'border-color: #363636')
        self.main_label.setEnabled(False)
        self.label = QtWidgets.QPushButton(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(SCREEN_WIDTH * 0.3,
                                            SCREEN_HEIGHT * 0.2,
                                            SCREEN_WIDTH * 0.35,
                                            SCREEN_HEIGHT * 0.07))
        self.label.setStyleSheet('font-size: 24px;'
                                 'font-family: "Trajan Pro 3";'
                                  'color: qlineargradient(spread:pad, '
                                  'x1:0, y1:0.5, x2:1, y2:0.5, stop:0 '
                                  'rgba(209, 166, 107, 255), stop:0.15 '
                                  'rgba(203, 155, 81, 255), stop:0.37 '
                                  'rgba(246, 226, 122, 255), stop:0.5 '
                                  'rgba(246, 242, 192, 255), stop:0.63 '
                                  'rgba(246, 226, 122, 255), stop:0.85 '
                                  'rgba(203, 155, 81, 255), stop:1 '
                                  'rgba(209, 166, 107, 255));'
                                 'border-style: outset;'
                                 'border-width: 0px;'
                                 'border-color: #363636')
        self.label.setEnabled(False)
        self.label.setObjectName("label")
        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(SCREEN_WIDTH * 0.28,
                                                 SCREEN_HEIGHT * 0.3,
                                                 SCREEN_WIDTH * 0.377,
                                                 SCREEN_HEIGHT * 0.04))
        self.name_input.setStyleSheet('background-color: white;'
                                      'border-style: outset;'
                               'border-width: 2px;'
                               'border-color: qlineargradient(spread:pad, '
                                      'x1:0, y1:0.5, x2:1, y2:0.5, stop:0 '
                                      'rgba(209, 166, 107, 255), stop:0.15 '
                                      'rgba(203, 155, 81, 255), stop:0.37 '
                                      'rgba(246, 226, 122, 255), stop:0.5 '
                                      'rgba(246, 242, 192, 255), stop:0.63 '
                                      'rgba(246, 226, 122, 255), stop:0.85 '
                                      'rgba(203, 155, 81, 255), stop:1 '
                                      'rgba(209, 166, 107, 255));')
        self.name_input.setObjectName("name_input")
        self.pushButton_ok = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ok.setGeometry(QtCore.QRect(180, 300, 75, 23))
        self.pushButton_ok.setStyleSheet('border-style: outset;'
                                         'background-color: white;'
                               'border-width: 2px;'
                               'border-color: qlineargradient(spread:pad, '
                                      'x1:0, y1:0.5, x2:1, y2:0.5, stop:0 '
                                      'rgba(209, 166, 107, 255), stop:0.15 '
                                      'rgba(203, 155, 81, 255), stop:0.37 '
                                      'rgba(246, 226, 122, 255), stop:0.5 '
                                      'rgba(246, 242, 192, 255), stop:0.63 '
                                      'rgba(246, 226, 122, 255), stop:0.85 '
                                      'rgba(203, 155, 81, 255), stop:1 '
                                      'rgba(209, 166, 107, 255));')
        self.pushButton_ok.setObjectName("pushButton_ok")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 379, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Введите имя"))
        self.pushButton_ok.setText(_translate("MainWindow", "Ок"))
