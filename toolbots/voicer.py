import os.path

from toolbots.bot import ToolBot
from gtts import gTTS

class Voicer(ToolBot):
    def __init__(self, mode):
        super(Voicer, self).__init__()
        self.mode = mode

    def result_load(self):
        try:
            self.progress.emit(50)
            self.status.emit('Генерация ответа')
            tts = gTTS(self.context, lang=self.mode)
            path = 'data/music/' + ''.join([x for x in f'{self.context}'.lower() if x.isalpha()]) + '.mp3'
            if not os.path.exists(path):
                print(1)
                print(path)
                tts.save(path)
                print(2)
            self.progress.emit(100)
            self.result.emit(path)
        except Exception as e:
            print(e)