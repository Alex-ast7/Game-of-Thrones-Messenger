from PyQt5.QtCore import QThread, pyqtSignal
from tqdm import tqdm


class ChatBot(QThread):
    answer = pyqtSignal(str)
    context = ''

    def run(self):
        for _ in tqdm(range(10 ** 7)):
            pass
        self.answer.emit(self.context)

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
