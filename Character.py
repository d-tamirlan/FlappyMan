import tkinter as tk
# from PIL import ImageTk, Image

class Character():
    x_pace = 50
    y_pace = 50

    def __init__(self, background, character_image_path):
        self.background = background
        self.character_image = tk.PhotoImage(file=character_image_path)
        self.character = self.background.create_image(100, 100, image=self.character_image)

        # self.config(bg='systemTransparent')
    #
    # def check_in_window(self, direction):
    #     x = self.winfo_x()
    #     y = self.winfo_y()
    #
    #     window = self.master
    #
    #     if direction == 'Up':
    #         if y-self.y_pace > 0:
    #             return True
    #         else:
    #             return False
    #
    #     elif direction == 'Right':
    #         window_width = window.winfo_width()
    #         character_width = self.winfo_width()
    #         if (x + character_width) + self.x_pace < window_width:
    #             return True
    #         else:
    #             return False
    #     elif direction == 'Down':
    #         window_height = window.winfo_height()
    #         character_height = self.winfo_height()
    #
    #         if (y+character_height) + self.y_pace < window_height:
    #             return True
    #         else:
    #             return False
    #     elif direction == 'Left':
    #         if x - self.x_pace > 0:
    #             return True
    #         else:
    #             return False
    #     # calculate x and y coordinates for the Tk root window
    #
    #     print('x', x)
    #     print('y', y)



    def move(self, event):
        x = self.winfo_x()
        y = self.winfo_y()

        if event.keysym == 'Up':
            if self.check_in_window('Up'):
                self.place(x=x, y=y-self.y_pace)

        elif event.keysym == 'Down':
            if self.check_in_window('Down'):
                self.place(x=x, y=y+self.y_pace)

        elif event.keysym == 'Right':
            if self.check_in_window('Right'):
                self.place(x=x+self.x_pace, y=y)

        elif event.keysym == 'Left':
            if self.check_in_window('Left'):
                self.place(x=x-self.x_pace, y=y)