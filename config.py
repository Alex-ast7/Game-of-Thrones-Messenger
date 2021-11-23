from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtWidgets import QMainWindow
import json


from chatbots.echo import Echo
from chatbots.speaker import Speaker
from chatbots.qa import QA
from db.db import DataBase
from design import SCREEN_WIDTH, SCREEN_HEIGHT
from db.user import UserDB


class UiDesignConfig(QMainWindow):
    def __init__(self, font_size, button_width):
        super().__init__()
        self.font_size = font_size
        self.font = QFont('Montserrat', self.font_size)
        self.button_width = button_width

    @property
    def font_height(self):
        return QFontMetrics(self.font).boundingRect('A').height()

    @property
    def size(self):
        return self.font_size

    def letter_width(self, letter):
        return QFontMetrics(self.font).boundingRect(letter).width()

    @property
    def hidden_menu(self):
        return QtCore.QRect(SCREEN_WIDTH * 0.068,
                                                  SCREEN_HEIGHT * 0.01,
                                                  SCREEN_WIDTH * 0.068,
                                                  SCREEN_HEIGHT * 0.03)
    @property
    def shown_menu(self):
        return QtCore.QRect(SCREEN_WIDTH * 0.62,
                                                  SCREEN_HEIGHT * 0.01,
                                                  SCREEN_WIDTH * 0.068,
                                                  SCREEN_HEIGHT * 0.03)




class UiAppConfig(QMainWindow):
    def __init__(self):
        super(UiAppConfig, self).__init__()
        self.name = json.load(open('db/config.json', 'r'))['name']
        print(self.name)
        try:
            self.db = DataBase()
            self.user_db = UserDB(self.db)
            is_ok = True
            for i in self.user_db.get():
                if self.name == i.name:
                    is_ok = False
                    break
            if is_ok:
                self.user_db.post(self.name)
        except Exception as e:
            print(e)
        self.bots = [Echo, Speaker]
        self.labels_text = []
        self.infoes = []
        self.translates = []
