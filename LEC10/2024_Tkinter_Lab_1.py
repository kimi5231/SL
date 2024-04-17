import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s(%(lineno)d): %(asctime)s - %(levelname)s - %(message)s'
)

from logging import info as info, debug as debug, warning as warning

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog


window = Tk()
window.title('My First App')
window.geometry('800x800+0+0')
window.resizable(False, False)


top_frame = Frame(master=window)
top_frame.pack()


label = Label(master=top_frame, text='Hello, Tkinter~'.center(50, '*'), width=50, font=('Segoe UI', 10))
label.pack(side=LEFT)
# label.place(x=100, y=100)


def rotate():
    text = label.cget('text')
    text = text[1:] + text[0]
    label.config(text=text)

button = Button(master=top_frame, text='Rotate', width = 30, command=rotate)
button.pack(side=LEFT)

option_frame = LabelFrame(text='Options')
option_frame.pack(ipadx=10, ipady=10)

def cb_clicked():
    info(f'checkbutton updated {checked.get()}')

checked = BooleanVar(value=True)
checkbutton = Checkbutton(master=option_frame, text='CheckButton', command=cb_clicked, variable=checked)
checkbutton.pack(side=LEFT, fill=X, expand=TRUE, padx=10)


def rb_clicked():
    info(f'checkbutton updated {color.get()}')

color = StringVar(value='red')
Radiobutton(master=option_frame, text='RED', value='red', command=rb_clicked, variable=color).pack(side=LEFT)
Radiobutton(master=option_frame, text='GREEN', value='green', command=rb_clicked, variable=color).pack(side=LEFT)
Radiobutton(master=option_frame, text='BLUE', value='blue', command=rb_clicked, variable=color).pack(side=LEFT)


text_frame = LabelFrame(text='Text')
text_frame.pack()


def update_text(event=None):
    label.config(text=entry.get())

entry = Entry(master=text_frame, font=('Segoe UI', 10))
entry.bind('<Return>', update_text)
entry.pack(fill=X, expand=TRUE, padx=10, pady=10)



from tkinter.scrolledtext import ScrolledText

wiki_python = '''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[31]
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[32][33]
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[34] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[35]
Python consistently ranks as one of the most popular programming languages, and has gained widespread use in the machine learning community.[36][37][38][39]
'''*2
text = ScrolledText(master=text_frame, font=('Segoe UI', 10))
text.delete("1.0", END)
text.insert(END, wiki_python)
text.pack(padx=10, pady=10)

# tagging
text.tag_config('found', background='yellow', foreground='red')
text.tag_add('found', '3.0', '3.0+16chars')


# 리스트 박스.
history_frame = LabelFrame(text='Pattern History')
history_frame.pack()

selected = StringVar(value='Hello')
pattern_listbox = Listbox(master=history_frame, selectmode=MULTIPLE, height=5, listvariable=selected)
pattern_listbox.insert(0,'Python')
pattern_listbox.insert(1,r'\d\d')
pattern_listbox.insert(END,'[a-z]+')
pattern_listbox.insert(END,'[0-9]+')
for i in range(5):
    pattern_listbox.insert(END, 'Hello')
pattern_listbox.select_set(1)
pattern_listbox.pack(side=LEFT)

list_scroll_bar = Scrollbar(master=history_frame, command=pattern_listbox.yview)
list_scroll_bar.pack(side=RIGHT, fill=Y)
pattern_listbox.configure(yscrollcommand=list_scroll_bar.set)


def item_selected(event=None):
    info(f'{pattern_listbox.curselection()}')
    for index in pattern_listbox.curselection():
        info(f'{pattern_listbox.get(index)}')


pattern_listbox.bind('<<ListboxSelect>>', item_selected)

# 콤보박스.
combo_var = StringVar(value='USA')
combo = Combobox(master=window, values=['korea', 'japan', 'china'], textvariable=combo_var)
combo.pack()


def combo_selected(event=None):
    info(f'{combo.get()} is selected...')


def enter_new_combo_item(event=None):
    combo['value'] += (combo.get(), ) # tuple merge


combo.bind('<<ComboboxSelected>>', combo_selected)
combo.bind('<Return>', enter_new_combo_item)

combo.configure(state='readonly')


# 메세지 박스.
import tkinter.messagebox as Messagebox

Messagebox.showinfo('Info', 'This is information.')
Messagebox.showinfo('Warn', 'This is warnning.')
Messagebox.showinfo('Error', 'This is error.')

answer = Messagebox.askokcancel('Ok Cancel', 'OK or Cancel?')
info(answer)
answer = Messagebox.askquestion('Question', 'OK?')
info(answer)
answer = Messagebox.askretrycancel('Retry Cancel', 'Retry or Cancel?')
info(answer)
answer = Messagebox.askyesno('Yes No', 'Yes or No?')
info(answer)
answer = Messagebox.askyesnocancel('Yes No Cancel', 'Yes? No? or Cancel?')
info(answer)

# 메뉴.
def open_file():
    file_names = filedialog.askopenfilename(
        title='Select Files',
        filetypes=(
            ("Python files", "*.py"),
            ("Text files", "*.txt"),
            ("All files", "*.*")
        )
    )
    info(f'{file_names}')


def save_file_as():
    filename = filedialog.asksaveasfilename(
        title='Save file as...',
        filetypes=(
            ("Python files", "*.py"),
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ),
        defaultextension='py'
    )


top_menu = Menu()

menu_File = Menu(master=top_menu, tearoff=False)
menu_File.add_command(label='New File', accelerator='Ctrl+N')
menu_File.add_command(label='Open...', accelerator='Ctrl+O', command=open_file)
menu_File.add_separator()
menu_File.add_command(label='Save', state='disabled', accelerator='Ctrl+S')
menu_File.add_command(label='Save As...', accelerator='Ctrl+Shift+S', command=save_file_as)
menu_File.add_command(label='Quit', accelerator='Ctrl+Q')
top_menu.add_cascade(label='File', menu=menu_File)

window.config(menu=top_menu)


menu_Colors = Menu(top_menu, tearoff=False)
found_color = StringVar(value='yellow')
menu_Colors.add_radiobutton(label='Yellow', value='yellow', variable=found_color)
menu_Colors.add_radiobutton(label='Green', value='green', variable=found_color)
top_menu.add_cascade(label="Colors", underline=1, menu=menu_Colors)


def color_updated(var, index, mode):
    info(f'{var=} {index=} {mode=}')
    info(f'{found_color.get()}')


found_color.trace_add('write', color_updated)



window.bind_all('<Control-q>', lambda e: window.quit())
window.bind('<Escape>', lambda e: window.quit())
window.mainloop()