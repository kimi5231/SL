from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def stop(event=None):
    window.quit()


def rotate(event=None):
    logging.info('Button Pressed.')
    # 라벨의 텍스트 가져오기.
    text = label.cget('text')
    text = text[1:] + text[0]
    # 라벨의 텍스트 재지정.
    label.config(text=text)


def change_text(event=None):
    new_text = entry.get()
    label.config(text=new_text.center(50, ' '))
    text_box.insert(END, new_text)


def clean_text_box(event=None):
    # 텍스트 지우기.
    # '행.열' 행의 시작은 1, 열의 시작은 0
    text_box.delete('1.0', END)


def cb_clicked(event=None):
    logging.info(f'{ignore_case.get()}')


def found_color_updated(var, index, mode):
    logging.info(f'{var=}, {mode=}, {index=}')
    logging.info(f'{found_color.get()}')


# 윈도우 생성.
window = Tk()

# 윈도우 사이즈 설정 및 위치 고정.
# '가로x세로+x위치+y위치'
window.geometry('640x480+100+100')
# 윈도우 사이즈 변경 허용 여부.
window.resizable(False, False)

# 서브 윈도우 생성.
first_line_frame = Frame(window)
# 서브 윈도우를 메인 윈도우에 넣기.
first_line_frame.pack()

# 윈도우에 넣을 라벨 설정.
label = Label(first_line_frame, text='Hello, Tkinter~~')
# 라벨을 윈도우에 넣기.
label.pack(side=LEFT)        # default = top
# 직접 위치 지정.
# label.place(x=200, y=200)

# 윈도우에 넣을 버튼 설정.
button = Button(first_line_frame, text='Rotate', command=rotate)
# 버튼을 윈도우에 넣기.
button.pack(side=LEFT)

# 윈도우에 넣을 엔트리 설정.
entry = Entry(window, width=50)
# 엔트리에 엔터 키 설정.
entry.bind('<Return>', change_text)
# 엔트리를 윈도우에 넣기.
entry.pack()

python_text = '''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[31]
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[32][33]
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[34] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[35]
Python consistently ranks as one of the most popular programming languages, and has gained widespread use in the machine learning community.[36][37][38][39]
'''
# 윈도우에 넣을 텍스트 박스 생성.
text_box = ScrolledText(window, width=50, height=10, font=('Consolas', 10))
# 텍스트 박스에 텍스트 넣기.
text_box.insert(END, python_text)
# 텍스트 박스를 윈도우의 남은 공간에 꽉차게 넣기.
text_box.pack(fill=BOTH, expand=True, padx=10, pady=10)
# 텍스트 박스 지우기 버튼.
button2 = Button(first_line_frame, text='Clean', command=clean_text_box)
button2.pack(side=RIGHT)
# 텍스트 박스의 일부분을 테그(하이라이트) 처리함.
# background=텍스트의 배경색, foreground=텍스트의 색
text_box.tag_config('found', background='yellow', foreground='red')
# 테그(하이라이트) 부분 지정.
text_box.tag_add('found', '3.0+3chars', '3.0+10chars')

# 정수 값을 받을 수 있는 객체 생성.
ignore_case = IntVar()
# 윈도우에 넣을 체크 버튼 생성.
case_check_button = Checkbutton(window, text='Ignore case', variable=ignore_case, command=cb_clicked)
# 0으로 설정.
ignore_case.set(0)
# 체크 버튼을 윈도우에 넣기.
case_check_button.pack()

# 문자열을 받을 수 있는 객체 생성.
found_color = StringVar(value='yellow')
# 윈도우에 넣을 라디오 버튼 생성.
# yellow_rb = Radiobutton(window, text='Yellow', variable=found_color)
Radiobutton(window, text='Yellow', value='yellow', variable=found_color).pack()
Radiobutton(window, text='Green', value='green', variable=found_color).pack()
Radiobutton(window, text='Red', value='red', variable=found_color).pack()
found_color.trace_add('write', found_color_updated)
# 라디오 버튼을 윈도우에 넣기.
#yellow_rb.pack()

# 윈도우 종료 키 설정.
window.bind('<Escape>', stop)
# 윈도우 루프.
window.mainloop()