import tkinter as tk
from Background import Background


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Flappy Man')
        self.state('zoomed')
        self.background = Background(self)
        # self.background_image = tk.PhotoImage(file='img/background.png')
        # self.background_label = tk.Label(self, image=self.background_image)
        # self.wm_attributes("-transparentcolor", "white")
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # self.background = Background(self)
        self.bind('<KeyPress>', self.background.character.move)
