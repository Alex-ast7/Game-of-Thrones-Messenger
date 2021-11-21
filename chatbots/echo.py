from tqdm import tqdm

from chatbots.bot import ChatBot


class Echo(ChatBot):
    def open_load(self):
        self.progress.emit(50)
        self.status.emit('Загрузка модели')
        for _ in tqdm(range(10 ** 7)):
            pass
        self.progress.emit(100)

    def answer_load(self):
        self.progress.emit(50)
        self.status.emit('Генерация ответа')
        for _ in tqdm(range(10 ** 7)):
            pass
        self.progress.emit(100)
        self.answer.emit(self.context)

Echo.__name__ = 'Эхо'