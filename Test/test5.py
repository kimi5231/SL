import tkinter as tk

def left_click(event):
    print("마우스 왼쪽 버튼이 클릭되었습니다.")

root = tk.Tk()
root.geometry("300x200")
root.mainloop()

# 마우스 왼쪽 버튼 클릭 이벤트에 대한 바인딩
root.bind("<Button-1>", left_click)