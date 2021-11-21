import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from window_design import Ui_MainWindow

class FirstWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = FirstWindow()
        ex.showMaximized()
        ex.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)