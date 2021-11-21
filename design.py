from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFontDatabase, QIcon
from PyQt5.QtWidgets import QListView
from win32api import GetSystemMetrics


SCREEN_HEIGHT = GetSystemMetrics(1) * 0.8
SCREEN_WIDTH = GetSystemMetrics(0) * 0.25
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet('background-color: #ffffff;')
        MainWindow.setCentralWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        fontDB = QFontDatabase()
        fontDB.addApplicationFont('data/fonts/Montserrat-Regular.ttf')
        fontDB.addApplicationFont('data/fonts/Montserrat-Bold.ttf')
        fontDB.addApplicationFont('data/fonts/Trajan.ttf')
        self.message_input = QtWidgets.QLineEdit(self.centralwidget)
        self.message_input.setGeometry(QtCore.QRect(SCREEN_WIDTH * 0.046,
                                                 SCREEN_HEIGHT * 0.945,
                                                 SCREEN_WIDTH * 0.714,
                                                 SCREEN_HEIGHT * 0.03))
        self.message_input.setObjectName("line_Edit")

        self.chat_window = QtWidgets.QListWidget(self.centralwidget)
        self.chat_window.setGeometry(QtCore.QRect(SCREEN_WIDTH * 0.046,
                                                 SCREEN_HEIGHT * 0.051,
                                                 SCREEN_WIDTH * 0.907,
                                                 SCREEN_HEIGHT * 0.89))
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(SCREEN_WIDTH * 0.761,
                                                  SCREEN_HEIGHT * 0.945,
                                                  SCREEN_WIDTH * 0.193,
                                                  SCREEN_HEIGHT * 0.03))
        self.send_button.setStyleSheet('border-style: outset;'
                               'border-width: 2px;'
                               'border-radius: 2px;'
                               'border-color: qlineargradient(spread:pad, '
                                  'x1:0, y1:0.5, x2:1, y2:0.5, stop:0 '
                                  '#d50000, stop:0.22 '
                                  '#7e0303, stop:0.5 '
                                  '#ff001a, stop:0.78 '
                                  '#7e0303, stop:1 '
                                  '#d50000);')
        self.send_button.setObjectName("send_button")
        self.send_button.setIcon(QIcon('data/images/sword.png'))
        self.send_button.setIconSize(QSize(self.send_button.width() + 30, self.send_button.height()))
        self.chat_window.setObjectName("listWidget")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.header = QtWidgets.QPushButton(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(SCREEN_WIDTH * 0.046,
                                             0, SCREEN_WIDTH * 0.907,
                                             SCREEN_HEIGHT * 0.051))
        self.header.setText('Game Of Thrones')
        self.header.setStyleSheet('background-color: #363636;'
                                  'font-family: "Trajan Pro 3";'
                                  'font-size: 24px;'
                                  'color: qlineargradient(spread:pad, '
                                  'x1:0, y1:0.5, x2:1, y2:0.5, stop:0 '
                                  'rgba(209, 166, 107, 255), stop:0.15 '
                                  'rgba(203, 155, 81, 255), stop:0.37 '
                                  'rgba(246, 226, 122, 255), stop:0.5 '
                                  'rgba(246, 242, 192, 255), stop:0.63 '
                                  'rgba(246, 226, 122, 255), stop:0.85 '
                                  'rgba(203, 155, 81, 255), stop:1 '
                                  'rgba(209, 166, 107, 255))')
        self.menu_window = QtWidgets.QListWidget(self.centralwidget)
        self.menu_window.setGeometry(QtCore.QRect(SCREEN_WIDTH * 0.046,
                                     0, SCREEN_WIDTH * 0.566,
                                                  SCREEN_HEIGHT * 0.98))

        self.menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.menu_button.setGeometry(QtCore.QRect(SCREEN_WIDTH * 0.068,
                                                  SCREEN_HEIGHT * 0.01,
                                                  SCREEN_WIDTH * 0.068,
                                                  SCREEN_HEIGHT * 0.03))
        self.menu_button.setStyleSheet('background-color: grey;'
                                       'font-size: 20px;'
                                       'color: qlineargradient(spread:pad, '
                                      'x1:0, y1:0.5, x2:1, y2:0.5, stop:0 '
                                      'rgba(209, 166, 107, 255), stop:0.15 '
                                      'rgba(203, 155, 81, 255), stop:0.37 '
                                      'rgba(246, 226, 122, 255), stop:0.5 '
                                      'rgba(246, 242, 192, 255), stop:0.63 '
                                      'rgba(246, 226, 122, 255), stop:0.85 '
                                      'rgba(203, 155, 81, 255), stop:1 '
                                      'rgba(209, 166, 107, 255));'
                                       'padding-bottom: 4px')
        self.menu_button.setText('->')
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        self.chat_window.setStyleSheet('QLabel {font-family: "Montserrat";'
                                      'font-weight: bold;'
                                      'border-radius: 5px;}'
                                      'QPushButton {font-family: "Montserrat";'
                                      'color: qlineargradient(spread:pad, '
                                      'x1:0, y1:0.5, x2:1, y2:0.5, stop:0 '
                                      'rgba(209, 166, 107, 255), stop:0.15 '
                                      'rgba(203, 155, 81, 255), stop:0.37 '
                                      'rgba(246, 226, 122, 255), stop:0.5 '
                                      'rgba(246, 242, 192, 255), stop:0.63 '
                                      'rgba(246, 226, 122, 255), stop:0.85 '
                                      'rgba(203, 155, 81, 255), stop:1 '
                                      'rgba(209, 166, 107, 255));'
                                      'background-color: rgb(105, 105, 105);'
                                      'border-style: outset;'
                                      'border-width: 1px;'
                                      'border-color: rgb(105, 105, 105);'
                                      'border-radius: 10px;'
                                      'border-top-left-radius: 0px;'
                                      'text-align: left;'
                                      'font-size: 18px}'
                                      'QListWidget {background-image: '
                                      'url("data/images/фон чата.png");}')
        self.chat_window.setFlow(QListView.LeftToRight)
        self.chat_window.setResizeMode(QListView.Adjust)
        self.chat_window.setSpacing(5)
        self.chat_window.setViewMode(QListView.IconMode)
        self.menu_window.setStyleSheet('background-color: #363636')
        self.message_input.setStyleSheet('border-style: outset;'
                               'border-width: 2px;'
                               'border-radius: 2px;'
                               'border-color: qlineargradient(spread:pad, '
                                  'x1:0, y1:0.5, x2:1, y2:0.5, stop:0 '
                                  '#d50000, stop:0.22 '
                                  '#7e0303, stop:0.5 '
                                  '#ff001a, stop:0.78 '
                                  '#7e0303, stop:1 '
                                  '#d50000);')
        self.send_button.setText('')
        self.menu_window.hide()
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(SCREEN_WIDTH * 0.25,
                                                  SCREEN_HEIGHT * 0.5,
                                                  SCREEN_WIDTH * 0.5,
                                                  SCREEN_HEIGHT * 0.03))
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.hide()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.send_button.setText(_translate("MainWindow", "Отправить"))




