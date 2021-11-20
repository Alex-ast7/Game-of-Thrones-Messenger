from random import randint

from PyQt5.QtCore import QThread, pyqtSignal
from tqdm import tqdm


class ChatBot(QThread):
    answer = pyqtSignal(str)
    progress = pyqtSignal(int)
    status = pyqtSignal(str)
    mode = None
    context = ''
    finished = pyqtSignal()

    def run(self):
        if self.mode == 'open':
            self.open_load()
        elif self.mode == 'answer':
            self.answer_load()

    def open_load(self):
        pass

    def answer_load(self):
        pass

