import PyQt5.QtWidgets as qt
import PyQt5.QtGui as qt_gui
import PyQt5.QtCore as q_core


class Character(qt.QLabel):
    step = 45

    def __init__(self, window, character_image_path):
        super().__init__(window)
        self.setObjectName('character')
        # self.setStyleSheet('#character {border: 1px solid black}')
        character_image = qt_gui.QPixmap(character_image_path)
        self.setPixmap(character_image)
        self.move(100, 100)
        self.resize(character_image.width(), character_image.height())
        self.show()

    def check_in_window(self, direction):
        x = self.x()
        y = self.y()

        window = self.window()

        if direction == 'Up':
            if y - self.step >= 0:
                return True
            else:
                return False

        elif direction == 'Right':
            window_width = window.width()
            character_width = self.width()
            character_right_bound = x + character_width

            if character_right_bound + self.step <= window_width:
                return True
            else:
                return False

        elif direction == 'Down':
            window_height = window.height()
            print('w_height', window_height)
            character_height = self.height()
            character_bottom_bound = y + character_height
            print('character_bottom_bound', character_bottom_bound)
            print('==================')
            if character_bottom_bound + self.step <= window_height:
                return True
            else:
                return False

        elif direction == 'Left':
            if x - self.step >= 0:
                return True
            else:
                return False

    def character_move(self, event):
        x = self.x()
        y = self.y()

        if event.key() == q_core.Qt.Key_Up:
            if self.check_in_window('Up'):
                self.move(x, y-self.step)

        elif event.key() == q_core.Qt.Key_Down:
            if self.check_in_window('Down'):
                self.move(x, y+self.step)

        elif event.key() == q_core.Qt.Key_Right:
            if self.check_in_window('Right'):
                self.move(x+self.step, y)

        elif event.key() == q_core.Qt.Key_Left:
            if self.check_in_window('Left'):
                self.move(x-self.step, y)
