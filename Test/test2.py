import tkinter as tk

# select a color as the transparent color
TRNAS_COLOR = '#abcdef'

root = tk.Tk()
root.overrideredirect(1)
root.attributes('-transparentcolor', TRNAS_COLOR)

image = tk.PhotoImage(file='Cuba.png')
tk.Label(root, image=image, bg=TRNAS_COLOR).pack()

# support dragging window

def start_drag(event):
    global dx, dy
    dx, dy = event.x, event.y

def drag_window(event):
    root.geometry(f'+{event.x_root-dx}+{event.y_root-dy}')

root.bind('<Button-1>', start_drag)
root.bind('<B1-Motion>', drag_window)

root.mainloop()