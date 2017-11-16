import PyQt5.QtWidgets as qt
from Character import Character


class Window(qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Flappy Man')
        self.showMaximized()
        self.setObjectName('ManiWindow')
        # self.setLayout(qt.QVBoxLayout(root))
        self.setStyleSheet("#ManiWindow {border-image: url(img/background.png);}")
        self.character = Character(self)

    def keyPressEvent(self, event):
        self.character.character_move(event)