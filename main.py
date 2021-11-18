import sys
import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut

from bots import bot
from bots.bot import ChatBot
from config import UiDesignConfig, UiAppConfig
from db.chat import ChatDB
from db.db import DataBase
from db.message import MessageDB
from db.user import UserDB
from chooseChat import OpenChat
from design import Ui_MainWindow, SCREEN_HEIGHT, SCREEN_WIDTH
from PyQt5.QtGui import QKeySequence
from models.message import Message


class Assistant(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_width = self.chat_window.width() * 0.6
        self.design = UiDesignConfig(18, self.button_width)
        self.app = UiAppConfig()
        self.setupChats(len(self.app.bots))
        self.menu()
        self.shortcut = QShortcut(QKeySequence('Return'), self)
        self.shortcut.activated.connect(self.send)
        self.send_button.clicked.connect(self.send)
        self.menu_button.clicked.connect(self.menu)
        self.db = DataBase()

        self.message_db = MessageDB(self.db)
        self.chat_db = ChatDB(self.db)
        self.user_db = UserDB(self.db)

    def start_open_chat(self):
        try:
            self.chat_window.clear()
            self.menu()
            self.progress_bar.show()
            self.main_bot = self.app.bots[self.sender().i]()
            self.main_bot.mode = 'Open'
            print(1)
            self.main_bot.progress.connect(self.change_progressbar_val)
            self.main_bot.status.connect(self.change_progressbar_status)
            self.main_bot.start()
        except Exception as e:
            print(e)

    def finish_open_chat(self):
        self.progress_bar.hide()
        self.fill_chat(self.main_bot.__class__.__name__)

    def create_info(self, name, date):
        info = QtWidgets.QLabel(self.centralwidget)
        info.setText(
            f'{name} {date}')
        info.setFont(self.design.font)
        info.setMaximumWidth(max(self.chat_window.width() * 0.5, info.width()))
        info.setMaximumHeight(self.design.size)
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(
            QSize(self.chat_window.width() * 0.5, self.design.size))
        self.chat_window.addItem(item)
        self.chat_window.setItemWidget(item, info)
        info.setStyleSheet('font-size: 12px;'
                           'font-family: "Montserrat";'
                           'color: rgb(105, 105, 105);'
                           'background-color: #bac2c8;'
                           )
        info.i = len(self.app.infoes)
        self.app.infoes.append(info)

    def create_message(self, message):
        message_text, max_line = self.trasform_widget(message)
        label_text = QtWidgets.QPushButton(self.centralwidget)
        label_text.setText(message_text)
        label_text.setMinimumWidth(20)
        label_text.setMaximumWidth(
            max(min(self.button_width, max_line), 0))
        h = (message_text.count('\n') + 1) * self.design.font_height
        label_text.setMaximumHeight(h)
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(QSize(self.button_width, h + 20))
        self.chat_window.addItem(item)
        self.chat_window.setItemWidget(item, label_text)
        self.chat_window.scrollToItem(item)
        label_text.i = len(self.app.labels_text)
        self.app.labels_text.append(label_text)

    def change_progressbar_val(self, value):
        self.progress_bar.setValue(value)

    def change_progressbar_status(self, status):
        print(self.progress_bar.width())
        self.progress_bar.setFormat(status)
        try:
            # self.progress_bar.setAlignment(Qt.AlignCenter)
            print(self.progress_bar.width())
        except Exception as e:
            print(e)

    def send(self):
        message = self.message_input.text()
        self.message_input.clear()
        if message:
            self.main_bot.mode = 'Create answer'
            self.create_info(self.app.name, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
            self.create_message(message)
            self.message_db.post(Message(id=0, name=self.app.name, text=message, time=datetime.datetime.now(), chat=self.main_bot.__class__.__name__))
            self.progress_bar.show()
            self.main_bot.context = message
            self.main_bot.answer.connect(self.get_answer)
            self.main_bot.start()

    def get_answer(self, answer):
        self.progress_bar.hide()
        try:
            self.create_info(self.main_bot.__class__.__name__,
                             datetime.datetime.now().strftime(
                                 "%d-%m-%Y %H:%M"))
            self.create_message(answer)
            self.message_db.post(
                Message(id=0, name=self.main_bot.__class__.__name__, text=answer,
                        time=datetime.datetime.now(),
                        chat=self.main_bot.__class__.__name__))
        except Exception as e:
            print(e)
    def setupChats(self, chats_count):
        self.chats = []
        for i in range(chats_count):
            chat = QtWidgets.QPushButton(self.centralwidget)
            chat.setGeometry(QtCore.QRect(SCREEN_WIDTH * 0.046,
                                          0 + 0.077 * SCREEN_HEIGHT * i,
                                          SCREEN_WIDTH * 0.566,
                                          SCREEN_HEIGHT * 0.077))
            chat.setStyleSheet('background-color: grey;'
                               'border-style: outset;'
                               'border-width: 2px;'
                               'border-radius: 2px;'
                               'border-color: qlineargradient(spread:pad, '
                                  'x1:0, y1:0.5, x2:1, y2:0.5, stop:0 '
                                  '#d50000, stop:0.22 '
                                  '#7e0303, stop:0.5 '
                                  '#ff001a, stop:0.78 '
                                  '#7e0303, stop:1 '
                                  '#d50000);'
                               'font-family: "Trajan Pro 3";'
                               'font-size: 18px;'
                               'color: qlineargradient(spread:pad, '
                                  'x1:0, y1:0.5, x2:1, y2:0.5, stop:0 '
                                  '#d50000, stop:0.22 '
                                  '#7e0303, stop:0.5 '
                                  '#ff001a, stop:0.78 '
                                  '#7e0303, stop:1 '
                                  '#d50000);')
            chat.hide()
            chat.i = i
            chat.setText(self.app.bots[i].__name__)
            chat.clicked.connect(self.start_open_chat)
            self.chats.append(chat)

    def menu(self):
        try:
            if self.menu_window.isHidden():
                self.menu_window.show()
                for i in range(len(self.chats)):
                    self.chats[i].show()
                self.menu_button.setGeometry(self.design.shown_menu)
                self.menu_button.setText('<-')
            else:
                self.menu_window.hide()
                for i in range(len(self.chats)):
                    self.chats[i].hide()
                self.menu_button.setGeometry(self.design.hidden_menu)
                self.menu_button.setText('->')
        except Exception as e:
            print(e)

    def trasform_widget(self, message):
        words = []
        for word in message.split():
            if self.get_line_width(word) > self.button_width:
                words.extend(self.get_tokens(word))
            else:
                words.append(word)
        len_ = 0
        new_message = ''
        for word in words:
            len_ += self.get_line_width(word)
            if len_ > self.button_width:
                new_message += '\n' + word + ' '
                len_ = self.get_line_width(word + ' ')
            else:
                new_message += word + ' '
        new_message = '\n'.join(
            [' ' + i.strip() for i in new_message.split('\n')])
        return new_message, self.get_line_width(
            max(new_message.split('\n'), key=self.get_line_width))

    def get_line_width(self, line):
        return sum(self.design.letter_width(s) for s in line)

    def get_tokens(self, word):
        tokens = []
        new_word = ''
        i = 0
        while i < len(word):
            while i < len(word) and self.get_line_width(
                    new_word + word[i]) <= self.button_width:
                new_word += word[i]
                i += 1
            tokens.append(new_word)
            new_word = ''
        return tokens

    def fill_chat(self, chat):

        try:
            messages = self.message_db.get(chat=self.chat_db.get(title=chat)[0].id)
            for message in messages:
                self.create_info(message.name, message.time)
                self.create_message(message.text)

        except Exception as e:
            print(e)

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = Assistant()
        ex.showMaximized()
        ex.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
