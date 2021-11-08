from PyQt5.QtCore import QThread, pyqtSignal
from tqdm import tqdm


class OpenChat(QThread):
    signal = pyqtSignal(int)

    def run(self):
        for _ in tqdm(range(10 ** 7)):
            pass
        self.signal.emit(1)
