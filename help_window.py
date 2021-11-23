from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Help(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Помощь')
        self.setGeometry(500, 100, 300, 300)
        self.text_window = QtWidgets.QTextBrowser(self)
        self.text_window.resize(300, 300)
        self.text_window.setStyleSheet('font-size: 12px')
        self.text_window.setText('В чате "Говорилка" вы можете пообщаться с '
                                 'искусственным интелектом на тему Игры '
                                 'престолов. Бот постарается отвечать на ваши '
                                 'сообщения фразами из сериала.\n\nВ чате '
                                 '"Отвечалка" бот будет отвечать на ваши '
                                 'несложные вопросы.\n\nВ чате "Рекомендалка" '
                                 'бот по вашему описанию сможет подобрать '
                                 'подходящие серии.\n\nСправа каждого '
                                 'сообщения есть две кнопки - перевод и звук. '
                                 'По нажатию на первую кнопку соответствующее '
                                 'сообщение будет переведено на выбранный '
                                 'язык. По нажатию на вторую - текст '
                                 'сообщения будет озвучен.')