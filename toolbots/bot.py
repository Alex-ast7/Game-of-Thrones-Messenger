from PyQt5.QtCore import QThread, pyqtSignal


# класс для второго потока
class ToolBot(QThread):
    # подключение сигналов
    progress = pyqtSignal(int)
    status = pyqtSignal(str)
    context = ''
    i = None
    result = pyqtSignal(str)

    def run(self):
        self.result_load()

    def result_load(self):
        pass
