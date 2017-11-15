import tkinter as tk
from PIL import Image, ImageTk


def key_press(e):
    print('press', e.keysym)


window = tk.Tk()
window.title('Test')
window.state('zoomed')
# window.configure(background='black')

character_image = tk.PhotoImage(file='img/character.png')

frame = tk.Frame(window)
frame.pack(fill=tk.BOTH, expand=tk.YES)


p = tk.PhotoImage(file='img/background.png')


canvas = tk.Canvas(frame)

# character = canvas.create_image(0, 0, image=character_image)

canvas.pack(fill=tk.BOTH, expand=tk.YES)

photoimage = ImageTk.PhotoImage(file="img/character.png")

# print(canvas.move(character, 500, 100))


background_image = canvas.create_image(50, 50, image=p)
character = canvas.create_image(100, 100, image=photoimage)

# bg = tk.Label(frame, image=background_image)
# bg.place(x=0, y=0, relwidth=1, relheight=1)



window.bind("<KeyPress>", key_press)
window.mainloop()

