from random import randint

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from chatbots.bot import ChatBot


# класс для работы бота Говрилка
class Speaker(ChatBot):
    # метод установки параметров
    def get_length_param(self, text: str) -> str:
        tokens_count = len(self.tokenizer.encode(text))
        if tokens_count <= 15:
            len_param = '1'
        elif tokens_count <= 50:
            len_param = '2'
        elif tokens_count <= 256:
            len_param = '3'
        else:
            len_param = '-'
        return len_param

    # метод загрузки бота
    def open_load(self):
        self.progress.emit(1)
        # изменения статусов бота
        self.status.emit('Загрузка токенизатора')
        checkpoint = "Grossmend/rudialogpt3_medium_based_on_gpt2"
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        self.progress.emit(30)
        self.status.emit('Загрузка модели')
        # подключение модели
        self.model = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path='checkpoints/gpt/', )
        self.model = self.model.to('cpu')
        self.model.eval()
        self.progress.emit(100)
        self.finished.emit()

    # метод получения ответа бота
    def answer_load(self):
        self.progress.emit(50)
        self.status.emit('Генерация ответа')
        # загрузка параметров бота
        chat_history_ids = torch.zeros((1, 0), dtype=torch.int)
        new_user_input_ids = self.tokenizer.encode(
            f"|0|{self.get_length_param(self.context)}|" +
            self.context + self.tokenizer.eos_token, return_tensors="pt")
        chat_history_ids = torch.cat([chat_history_ids, new_user_input_ids],
                                     dim=-1)
        next_len = randint(1, 2)
        new_user_input_ids = self.tokenizer.encode(f"|1|{next_len}|",
                                                   return_tensors="pt")
        chat_history_ids = torch.cat([chat_history_ids, new_user_input_ids],
                                     dim=-1)
        input_len = chat_history_ids.shape[-1]
        chat_history_ids = self.model.generate(
            chat_history_ids,
            num_return_sequences=1,
            max_length=512,
            no_repeat_ngram_size=3,
            do_sample=True,
            top_k=50,
            top_p=0.9,
            temperature=0.6,  # 0 for greedy
            mask_token_id=self.tokenizer.mask_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
            unk_token_id=self.tokenizer.unk_token_id,
            pad_token_id=self.tokenizer.pad_token_id,
            device='cpu'
        )

        self.tokenizer.decode(chat_history_ids[:, input_len:][0],
                              skip_special_tokens=True)
        self.progress.emit(100)

        self.answer.emit(str(self.tokenizer.decode(chat_history_ids[:,
                                                   input_len:][0],
                                                   skip_special_tokens=True)))
        self.finished.emit()


Speaker.__name__ = 'Говорилка'
