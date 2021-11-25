import sqlite3

from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from transformers import AutoTokenizer, AutoModel

from chatbots.bot import ChatBot


# класс для работы бота Рекомендашка
class Rater(ChatBot):
    # метод загрузки бота
    def open_load(self):
        self.progress.emit(1)
        # изменения статусов бота
        self.status.emit('Загрузка токенизатора')
        checkpoint = "DeepPavlov/rubert-base-cased-sentence"
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        self.progress.emit(30)
        self.status.emit('Загрузка модели')
        # подключение модели
        self.model = AutoModel.from_pretrained(checkpoint)
        self.model = self.model.to('cpu')
        self.model.eval()
        self.progress.emit(100)
        self.finished.emit()

    # метод загрузки ответа
    def answer_load(self):
        try:
            self.progress.emit(50)
            self.status.emit('Генерация ответа')
            output = self.model(**self.tokenizer(self.context, max_length=512,
                                                 return_tensors='pt',
                                                 truncation=True))
            vector = []
            for elem in output[1].view(-1):
                vector.append(elem.item())
            vectors = pd.read_csv('data/vectors.csv')
            # поиск ближайшего вектора
            min_d = 0
            min_id = 0
            for row in vectors.iterrows():
                distance = cosine_similarity([list(row[1])[1:]],
                                             [vector])[0][0]
                if distance > min_d:
                    min_d = distance
                    min_id = list(row[1])[0]
            # получение серии из бд
            con = sqlite3.connect('db/messenger.db')
            cur = con.cursor()
            answer = cur.execute(f'select Название from Episodes where '
                                 f'id={min_id}').fetchone()[0]
            con.close()
            self.progress.emit(100)
            self.answer.emit(answer)
        except Exception as e:
            print(e)


Rater.__name__ = 'Рекомендашка'
