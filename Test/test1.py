import tkinter as tk
import os

# Tkinter 윈도우 생성
root = tk.Tk()
# root.attributes("-fullscreen", True)  # 전체 화면으로 설정

# 오리 이미지 파일 경로
image_path = "Cuba.png"  # 오리 이미지 파일 경로로 변경해야 합니다

# 오리 이미지를 화면에 표시할 Canvas 생성
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack()

# 오리 이미지 로드
duck_image = tk.PhotoImage(file=image_path)

# Canvas에 오리 이미지를 그립니다.
# x, y 좌표는 Canvas의 중앙으로 설정합니다.
duck = canvas.create_image(root.winfo_screenwidth() / 2, root.winfo_screenheight() / 2, image=duck_image)

# 마우스 움직임을 감지하여 오리를 이동시키는 함수
def move_duck(event):
    x, y = event.x, event.y
    canvas.coords(duck, x, y)  # 오리 이미지의 좌표를 마우스 위치로 설정

# 마우스 움직임 이벤트 바인딩
canvas.bind("<Motion>", move_duck)

# 윈도우를 항상 최상위로 유지
root.attributes("-topmost", True)

# 윈도우 시작
root.mainloop()