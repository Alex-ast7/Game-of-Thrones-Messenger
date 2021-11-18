from tqdm import tqdm

from chatbots.bot import Bot


class QA(Bot):
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

    def answer_load(self):
        self.progress.emit(1)
        self.status.emit('Генерация ответа')
        for _ in tqdm(range(10 ** 7)):
            pass
        self.progress.emit(100)
        self.answer.emit('Как дела?')

QA.__name__ = 'Отвечалка'