from PyQt5.QtCore import QThread, pyqtSignal
from tqdm import tqdm


class Bot(QThread):
    answer = pyqtSignal(str)
    progress = pyqtSignal(int)
    status = pyqtSignal(str)
    mode = None
    context = ''

    def run(self):
        if self.mode == 'open':
            self.open_load()
        elif self.mode == 'answer':
            self.answer_load()

    def open_load(self):
        pass

    def answer_load(self):
        pass


