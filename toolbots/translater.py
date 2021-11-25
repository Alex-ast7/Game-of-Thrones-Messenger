from toolbots.bot import ToolBot
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# класс модели для перевода
class Translater(ToolBot):
    def __init__(self, mode):
        super(Translater, self).__init__()
        self.mode = mode

    # метод загрузки модели
    def result_load(self):
        try:
            self.progress.emit(10)
            self.status.emit('Загрузка токенизатора')
            tokenizer = AutoTokenizer.from_pretrained(f"Helsinki-NLP/opus-mt-"
                                                      f"{self.mode}",
                                                      cache_dir='cache')
            # изменение значений и статуса полосы прогрузки
            self.progress.emit(40)
            self.status.emit('Загрузка модели')
            model = AutoModelForSeq2SeqLM.from_pretrained(
                f"Helsinki-NLP/opus-mt-{self.mode}")
            self.progress.emit(70)
            self.status.emit('Генерация ответа')
            input_ids = tokenizer.encode(self.context, return_tensors="pt")
            outputs = model.generate(input_ids)
            decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
            self.progress.emit(100)
            self.result.emit(decoded)
        except Exception as e:
            print(e)