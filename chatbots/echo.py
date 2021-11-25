from tqdm import tqdm

from chatbots.bot import ChatBot


# класс тестового бота Эхо
class Echo(ChatBot):
    # метод открытия бота
    def open_load(self):
        # эмитация загрузки
        self.progress.emit(50)
        self.status.emit('Загрузка модели')
        for _ in tqdm(range(10 ** 7)):
            pass
        self.progress.emit(100)

    # метод получения ответа
    def answer_load(self):
        # эмитация загрузки отвтеа
        self.progress.emit(50)
        self.status.emit('Генерация ответа')
        for _ in tqdm(range(10 ** 7)):
            pass
        self.progress.emit(100)
        self.answer.emit(self.context)

Echo.__name__ = 'Эхо'
