import tkinter as tk
import pyautogui

# select a color as the transparent color
TRNAS_COLOR = '#abcdef'

root = tk.Tk()
root.overrideredirect(1)
root.attributes('-transparentcolor', TRNAS_COLOR)
root.attributes("-topmost", True)

image = tk.PhotoImage(file='Cuba.png')
tk.Label(root, image=image, bg=TRNAS_COLOR).pack()

# support dragging window

x, y = 0, 0

def start_drag(event):
    global dx, dy
    dx, dy = event.x, event.y

def drag_window(event):
    root.geometry(f'+{event.x_root-dx}+{event.y_root-dy}')

def move_self():
    global x, y
    x += 1
    y += 1
    root.geometry(f'+{x}+{y}')
    pyautogui.moveTo(x, y)
    root.after(10, move_self)


root.bind('<Button-1>', start_drag)
root.bind('<B1-Motion>', drag_window)


move_self()
root.mainloop()

