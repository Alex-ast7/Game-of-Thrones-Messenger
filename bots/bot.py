from PyQt5.QtCore import QThread, pyqtSignal
from tqdm import tqdm


class ChatBot(QThread):
    answer = pyqtSignal(str)
    progress = pyqtSignal(int)
    status = pyqtSignal(str)
    mode = None
    context = ''

    def run(self):
        if self.mode == 'Open':
            for _ in tqdm(range(10 ** 7)):
                pass
            self.answer.emit(self.context)
            self.progress.emit(30)
            self.status.emit('g')
            for _ in tqdm(range(10 ** 7)):
                pass
            self.progress.emit(60)
            self.status.emit('g')
        # elif self.mode == 'Create answer':
        #     for _ in tqdm(range(10 ** 7)):
        #         pass
        #     self.answer.emit(self.context)
        #     self.status.emit('первая фаза')
        #     for _ in tqdm(range(10 ** 7)):
        #         pass
        #     self.status.emit('вторая фаза')

class QABot:
    def __init__(self):
        pass

    def answer(self, message):
        for _ in range(10 ** 8):
            pass
        return 'Привет'

ChatBot.__name__ = 'Говорилка'
QABot.__name__ = 'Отвечалка'
print(ChatBot().__class__.__name__)
