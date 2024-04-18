import tkinter as tk
from tkinter import ttk
import pyautogui

def change_cursor(event):
    root.config(cursor="hand2")  # 커서를 hand2로 변경
    pyautogui.moveTo(100, 100)

root = tk.Tk()

button = ttk.Button(root, text="Hover over me!")
button.pack(padx=20, pady=20)

button.bind("<Enter>", change_cursor)

root.mainloop()
