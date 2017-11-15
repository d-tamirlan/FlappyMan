import tkinter as tk
from Character import Character
from PIL import ImageTk, Image


class Background(tk.Canvas):
    def __init__(self, window):
        super().__init__(window)
        frame = tk.Frame(window)
        self.pack(fill=tk.BOTH, expand=tk.YES)

        self.background_image = ImageTk.PhotoImage(file='img/background.png')
        self.background_image = (2, 10)
        self.background_image = self.background_image.subsample(1,5)
        # self.background_image.zoom(window.winfo_width(), window.winfo_height())
        self.character = Character(self, 'img/character.png')
        bg_image = self.create_image(0,0, image=self.background_image)
        self.tag_lower(bg_image)
