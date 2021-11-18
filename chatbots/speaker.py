from tqdm import tqdm

from chatbots.bot import Bot


class Speaker(Bot):

    def open_load(self):
        self.progress.emit(1)
        self.status.emit('Загрузка токенизатора')
        for _ in tqdm(range(10 ** 7)):
            pass
        self.progress.emit(30)
        self.status.emit('Загрузка модели')
        for _ in tqdm(range(10 ** 7)):
            pass
        self.progress.emit(100)

    def answer_load(self):
        self.progress.emit(1)
        self.status.emit('Генерация ответа')
        for _ in tqdm(range(10 ** 7)):
            pass
        self.progress.emit(100)
        self.answer.emit('Давай поговорим')


Speaker.__name__ = 'Говорилка'
