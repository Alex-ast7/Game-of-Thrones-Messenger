import datetime
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut, QInputDialog
from config import UiDesignConfig, UiAppConfig
from db.chat import ChatDB
from db.db import DataBase
from db.message import MessageDB
from db.user import UserDB
from design import Ui_MainWindow, SCREEN_HEIGHT, SCREEN_WIDTH
from help_window import Help
from models.message import Message
import keyboard
from pygame import mixer

from toolbots.translater import Translater


class Assistant(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Ассистент')
        self.button_width = self.chat_window.width() * 0.6
        self.design = UiDesignConfig(18, self.button_width)
        self.app = UiAppConfig()
        self.setupChats(len(self.app.bots))
        self.menu()
        self.shortcut = QShortcut(QKeySequence("Return"), self)
        self.shortcut.activated.connect(self.send)
        mixer.init()
        keyboard.add_hotkey("ctrl+M", lambda: self.play_music())
        keyboard.add_hotkey("ctrl+P", lambda: self.stop_music())
        self.send_button.clicked.connect(self.send)
        self.menu_button.clicked.connect(self.menu)
        self.help_button.clicked.connect(self.open_help)
        self.db = DataBase()
        self.message_db = MessageDB(self.db)
        self.chat_db = ChatDB(self.db)
        self.user_db = UserDB(self.db)
        self.is_play = True

    def play_music(self):
        if self.is_play:
            mixer.music.load('data/music/main_music.mp3')
            mixer.music.play()
        else:
            mixer.music.unpause()

    def stop_music(self):
        mixer.music.pause()
        self.is_play = False

    def open_help(self):
        try:
            self.window2 = Help()
            self.window2.show()
        except Exception as e:
            print(e)

    def open_chat(self):
        self.chat_window.clear()
        self.menu()
        self.main_bot = self.app.bots[self.sender().i]()
        self.main_bot.mode = 'open'
        self.fill_chat(self.main_bot.__class__.__name__)
        self.progress_bar.show()

        self.main_bot.progress.connect(self.change_progressbar_val)
        self.main_bot.status.connect(self.change_progressbar_status)
        self.main_bot.answer.connect(self.get_answer)
        self.main_bot.finished.connect(self.main_bot.quit)
        self.main_bot.start()

    def create_info(self, name, date):
        info = QtWidgets.QLabel(self.centralwidget)
        info.setText(
            f'{name} {date}')
        info.setFont(self.design.font)
        info.setMaximumWidth(max(self.chat_window.width() * 0.5, info.width()))
        info.setMaximumHeight(self.design.size)
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(
            QSize(self.chat_window.width() * 0.9, self.design.size))
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
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        item.setSizeHint(QSize(self.button_width, h + 20))
        self.chat_window.addItem(item)
        self.chat_window.setItemWidget(item, label_text)
        self.chat_window.scrollToItem(item)
        label_text.i = len(self.app.labels_text)
        self.app.labels_text.append(label_text)

    def create_translate_function(self):
        translate_button = QtWidgets.QPushButton(self.centralwidget)
        translate_button.setStyleSheet('background-color: #bac2c8;'
                                       'border-radius: 5px;'
                                       'padding: 7px')
        translate_button.setIcon(QIcon('data/images/translation.png'))
        translate_button.clicked.connect(self.open_translate_window)
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(QSize(32, 32))
        self.chat_window.addItem(item)
        self.chat_window.setItemWidget(item, translate_button)
        translate_button.i = len(self.app.translates)
        self.app.translates.append(translate_button)

    def open_translate_window(self):
        self.choice, ok_pressed = QInputDialog.getItem(
            self, "Выбор", "Выберите вариант перевода",
            ("ru-en", "en-ru"), 0, False)
        self.translate_text()


    def create_audio_function(self):
        audio = QtWidgets.QPushButton(self.centralwidget)
        audio.setStyleSheet('background-color: #bac2c8;'
                            'border-radius: 5px;'
                            'padding: 7px')
        audio.setIcon(QIcon('data/images/audio.png'))
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(QSize(32, 32))
        self.chat_window.addItem(item)
        self.chat_window.setItemWidget(item, audio)

    def change_progressbar_val(self, value):
        self.progress_bar.setValue(value)
        if value == 100:
            self.progress_bar.hide()

    def change_progressbar_status(self, status):
        self.progress_bar.setFormat(status)

    def send(self):
        message = self.message_input.text()
        self.message_input.clear()
        if message:
            self.main_bot.mode = 'answer'
            self.create_info(self.app.name,
                                datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
            self.create_message(message)
            self.create_translate_function()
            self.create_audio_function()
            try:
                self.message_db.post(Message(id=0, name=self.app.name, text=message,
                                             time=datetime.datetime.now(),
                                             chat=self.main_bot.__class__.__name__))
            except Exception as e:
                print(e)
            self.progress_bar.show()
            self.main_bot.context = message
            self.main_bot.quit()
            self.main_bot.start()

    def get_answer(self, answer):

        try:
            self.create_info(self.main_bot.__class__.__name__,
                             datetime.datetime.now().strftime(
                                 "%d-%m-%Y %H:%M"))
            self.create_message(answer)
            self.message_db.post(
                Message(id=0, name=self.main_bot.__class__.__name__,
                        text=answer,
                        time=datetime.datetime.now(),
                        chat=self.main_bot.__class__.__name__))
            self.create_translate_function()
            self.create_audio_function()
        except Exception as e:
            print(e)

    def translate_text(self):
        print(self.choice)
        self.tool = Translater(self.choice)
        self.progress_bar.show()
        self.tool.i = self.sender().i
        self.tool.context = self.app.labels_text[self.tool.i].text()
        self.tool.progress.connect(self.change_progressbar_val)
        self.tool.status.connect(self.change_progressbar_status)
        self.tool.result.connect(self.get_translate)
        self.tool.quit()
        self.tool.start()

    def get_translate(self, result):
        message_text, max_line = self.trasform_widget(result)
        h = (message_text.count('\n') + 1) * self.design.font_height
        self.app.labels_text[self.tool.i].setText(message_text)
        self.app.labels_text[self.tool.i].setMinimumWidth(max_line)
        self.app.labels_text[self.tool.i].setMaximumWidth(
            max(min(self.button_width, max_line), 0))
        self.app.labels_text[self.tool.i].setMaximumHeight(h)
        item = self.chat_window.item(self.tool.i * 4 + 1)
        message = self.message_db.get(
            chat=self.chat_db.get(title=self.main_bot.__class__.__name__)[0].id)[self.tool.i]
        self.message_db.put(message, text=message_text)


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
            chat.clicked.connect(self.open_chat)
            self.chats.append(chat)

    def menu(self):
        try:
            if self.menu_window.isHidden():
                self.menu_window.show()
                for i in range(len(self.chats)):
                    self.chats[i].show()
                self.menu_button.setGeometry(self.design.shown_menu)
                self.menu_button.setText('<-')
                self.menu_button.setStyleSheet('background-color: grey;'
                                               'font-size: 20px;'
                                               'color: qlineargradient(spread:pad, '
                               'x1:0, y1:0.5, x2:1, y2:0.5, stop:0 '
                               '#d50000, stop:0.22 '
                               '#7e0303, stop:0.5 '
                               '#ff001a, stop:0.78 '
                               '#7e0303, stop:1 '
                               '#d50000);'
                                               'padding-bottom: 4px')
            else:
                for i in range(len(self.chats)):
                    self.chats[i].hide()
                self.menu_window.hide()
                self.menu_button.setGeometry(self.design.hidden_menu)
                self.menu_button.setText('->')
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
            messages = self.message_db.get(
                chat=self.chat_db.get(title=chat)[0].id)
            for message in messages:
                self.create_info(message.name,
                                 message.time.strftime("%d-%m-%Y %H:%M"))
                self.create_message(message.text)
                self.create_translate_function()
                self.create_audio_function()
        except Exception as e:
            print(e)


# if __name__ == '__main__':
#     try:
#         app = QApplication(sys.argv)
#         ex = Assistant()
#         ex.showMaximized()
#         ex.show()
#         sys.exit(app.exec_())
#     except Exception as e:
#         print(e)
