from transformers import pipeline

from chatbots.bot import ChatBot


# класс для работы бота Отвечалка
class QA(ChatBot):
    # метод изменения статусов бота
    def open_load(self):
        self.progress.emit(1)
        self.status.emit('Загрузка модели')
        model_name = "deepset/roberta-base-squad2"
        self.model = pipeline('question-answering', model=model_name,
                              tokenizer=model_name, cache_dir='cache')
        self.progress.emit(100)

    # метод загрузки отвтеа
    def answer_load(self):
        self.progress.emit(1)
        self.status.emit('Генерация ответа')
        question, context = self.context.split('->')
        QA_input = {
            'question': question,
            'context': context
        }
        result = self.model(QA_input)
        self.progress.emit(100)
        print(result)
        self.answer.emit(result['answer'])


QA.__name__ = 'Отвечалка'
