import subprocess
import pyautogui
import time

# 메모장 실행
subprocess.Popen(["notepad.exe"])

# 메모장이 열릴 때까지 대기 (시간은 상황에 따라 조절할 수 있습니다)
time.sleep(2)

# 텍스트 입력
pyautogui.write("Hello, World!")