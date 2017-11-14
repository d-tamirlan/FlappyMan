import tkinter as tk
from Character import Character


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Flappy Man')
        self.state('zoomed')
        self.character = Character(self, 'img/character.png')
        self.bind('<KeyPress>', self.character.move)
