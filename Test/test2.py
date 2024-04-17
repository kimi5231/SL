import tkinter as tk

class TransparentWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.overrideredirect(True)  # 윈도우 프레임 제거
        self.attributes("-alpha", 0.5)  # 투명도 설정
        self.attributes("-topmost", True)  # 항상 위에 표시

        # 오리 이미지 크기 가져오기
        self.duck_image = tk.PhotoImage(file="cuba.png")  # 오리 이미지 파일 경로로 변경
        self.duck_width = self.duck_image.width()
        self.duck_height = self.duck_image.height()

        # 윈도우 크기 및 위치 설정
        self.geometry("{}x{}+0+0".format(self.duck_width, self.duck_height))

        # Canvas 생성
        self.canvas = tk.Canvas(self, width=self.duck_width, height=self.duck_height, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # 오리 이미지를 Canvas에 그림
        self.duck = self.canvas.create_image(self.duck_width / 2, self.duck_height / 2, image=self.duck_image)

        # 마우스 이벤트를 통과시키기 위해 마우스 이벤트 바인딩
        self.canvas.bind("<Button-1>", self.move_window)
        self.canvas.bind("<B1-Motion>", self.move_window)

    def move_window(self, event):
        self.geometry("+{0}+{1}".format(event.x_root - self.duck_width / 2, event.y_root - self.duck_height / 2))

if __name__ == "__main__":
    app = TransparentWindow()
    app.mainloop()
