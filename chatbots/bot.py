from PyQt5.QtCore import QThread, pyqtSignal


# общий класс для работы ботов
class ChatBot(QThread):
    # подключение сигналов
    answer = pyqtSignal(str)
    progress = pyqtSignal(int)
    status = pyqtSignal(str)
    mode = None
    context = ''
    finished = pyqtSignal()

    # метод изменения режимов бота
    def run(self):
        if self.mode == 'open':
            self.open_load()
        elif self.mode == 'answer':
            self.answer_load()

    def open_load(self):
        pass

    def answer_load(self):
        pass
