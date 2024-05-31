from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image


def show_img2(img1, img2):
    window = Tk()
    tk_image1 = ImageTk.PhotoImage(img1)
    tk_image2 = ImageTk.PhotoImage(img2)
    Label(window, image=tk_image1).pack(side=LEFT)
    Label(window, image=tk_image2).pack(side=LEFT)

    def stop(event=None):
        window.destroy()

    window.bind('<Escape>', stop)
    window.bind('q', stop)
    window.mainloop()


def show_img1(img):
    window = Tk()
    tk_image = ImageTk.PhotoImage(img)
    Label(window, image=tk_image).pack(side=LEFT)

    def stop(event=None):
        window.destroy()

    window.bind('<Escape>', stop)
    window.bind('q', stop)
    window.mainloop()