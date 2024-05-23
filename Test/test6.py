from PIL import ImageGrab

# 화면 캡처하기
screenshot = ImageGrab.grab()

# 캡처한 화면을 이미지 파일로 저장하기
screenshot.save("screenshot.png")

# 캡처한 화면을 화면에 표시하기
screenshot.show()
