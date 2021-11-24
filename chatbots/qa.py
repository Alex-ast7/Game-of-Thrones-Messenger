from tqdm import tqdm

from chatbots.bot import ChatBot


# класс для работы бота Отвечалка
class QA(ChatBot):
    # метод изменения статусов бота
    def open_load(self):
        self.progress.emit(1)
        self.status.emit('Загрузка поисковика')
        for _ in tqdm(range(10 ** 7)):
            pass
        self.progress.emit(30)
        self.status.emit('Загрузка модели')
        for _ in tqdm(range(10 ** 7)):
            pass
        self.progress.emit(100)

    # метод загрузки отвтеа
    def answer_load(self):
        self.progress.emit(1)
        self.status.emit('Генерация ответа')
        for _ in tqdm(range(10 ** 7)):
            pass
        self.progress.emit(100)
        self.answer.emit('Как дела?')


QA.__name__ = 'Отвечалка'
