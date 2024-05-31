from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from PIL import ImageTk, Image, ImageGrab
import random


def stop(event=None):
    window.destroy()


def save_image(event=None):
    file_path = asksaveasfilename(filetypes=[('PNG Images', '*.png'), ('All Files', '*.*')])
    if file_path:
        background_img.save(file_path + '.png', 'png')


def select_image(event=None):
    file_path = askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg;*.gif;*.bmp')])
    if file_path:
        image = Image.open(file_path)
        num = random.randint(1, 4)
        if num == 1:
            image = image.resize((200, 200))
        elif num == 2:
            image = image.resize((200, 400))
        elif num == 3:
            image = image.resize((400, 200))
        elif num == 4:
            image = image.resize((400, 400))
        photo = ImageTk.PhotoImage(image)

        label = Label(window, image=photo)
        label.image = photo
        x = random.randint(-100, 700)
        y = random.randint(-100, 500)
        label.place(x=x, y=y)

        background_img.paste(image, (x,y))


window = Tk()
window.geometry("800x600+0+0")

menu = Menu()
menu_File = Menu(menu, tearoff=False)
menu_File.add_command(label="Open", accelerator='Ctrl+O', command=select_image)
menu_File.add_command(label="Save", accelerator='Ctrl+S', command=save_image)
menu_File.add_command(label='Quit', accelerator='Ctrl+Q', command=stop)
menu_File.add_separator()
menu.add_cascade(label='File', underline=True, menu=menu_File)
window.config(menu=menu)

window.bind('<Control-o>', select_image)
window.bind('<Control-s>', save_image)
window.bind('<Control-q>', stop)

background_img = Image.new('RGBA', (800, 600), 'black')

window.mainloop()