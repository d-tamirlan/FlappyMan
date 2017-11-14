import tkinter as tk


class Character(tk.Label):
    def __init__(self, window, character_image_path):
        self.character_image = tk.PhotoImage(file=character_image_path)
        super().__init__(window, image=self.character_image)
        self.pack()

    def move(self, event):
        x = self.winfo_rootx()
        y = self.winfo_rooty()

        if event.keysym == 'Up':
            print('up', event.keysym)
            print('x', x)
            print('y_last', y)
            print('y_now', y-10)

            self.place(x=x, y=y-10)

        elif event.keysym == 'Down':
            print('down', event.keysym)
            self.place(x=x, y=y+10)
