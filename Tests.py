import tkinter as tk
# from PIL import Image, ImageTk


def key_press(e):
    print('press', e.keysym)


window = tk.Tk()
window.title('Test')
window.state('zoomed')

character_image = tk.PhotoImage(file='img/character.png')
character = tk.Label(window, image=character_image)
character.pack()

window.bind("<KeyPress>", key_press)
window.mainloop()

