import sys

from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow, QApplication, QShortcut
import json

from assistant import Assistant
from window_design import Ui_MainWindow2


# класс функционала окна ввода имени
class FirstWindow(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        try:
            # подключсение кнопок и горячих клавиш
            self.setWindowTitle('Логин')
            self.pushButton_ok.clicked.connect(self.open_window)
            self.pushButton_ok.clicked.connect(self.change_name)
            self.shortcut = QShortcut(QKeySequence("Return"), self)
            self.shortcut.activated.connect(self.change_name)
            self.shortcut.activated.connect(self.open_window)
        except Exception as e:
            print(e)

    # метод открытия основного окна
    def open_window(self):
        self.close()
        self.window = Assistant()
        self.window.show()

    # метод смены имени
    def change_name(self):
        try:
            user_name = self.name_input.text()
            # запись имени в json файл
            json.dump({'name': user_name}, open('db/config.json', 'w'),
                      ensure_ascii=False)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = FirstWindow()
        ex.showMaximized()
        ex.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
