from toolbots.bot import ToolBot
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Translater(ToolBot):
    def __init__(self, mode):
        super(Translater, self).__init__()
        self.mode = mode
    def result_load(self):
        self.progress.emit(10)
        self.status.emit('Загрузка токенизатора')
        tokenizer = AutoTokenizer.from_pretrained(f"Helsinki-NLP/opus-mt-{self.mode}")
        self.progress.emit(40)
        self.status.emit('Загрузка модели')
        model = AutoModelForSeq2SeqLM.from_pretrained(
            "Helsinki-NLP/opus-mt-ru-en")
        self.progress.emit(70)
        self.status.emit('Генерация ответа')
        input_ids = tokenizer.encode(self.context, return_tensors="pt")
        outputs = model.generate(input_ids)
        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
        self.progress.emit(100)
        self.result.emit(decoded)