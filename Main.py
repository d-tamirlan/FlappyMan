import PyQt5.QtWidgets as qt
import sys
from Window import Window
from Character import Character


if __name__ == '__main__':
    app = qt.QApplication(sys.argv)
    window = Window()
    # character = Character(win, 'img/character.png')
    # bg.add_character()
    # character = Character(background.window)
    # bg.character.pack()
    # print('width', win.winfo_screenwidth())
    # print('height', win.winfo_screenheight())
    sys.exit(app.exec_())

