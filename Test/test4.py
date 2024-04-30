import subprocess
import pyautogui
import time

subprocess.Popen(["notepad.exe"])
np = pyautogui.getActiveWindow()
time.sleep(2)
np.resizeTo(300, 300)
pyautogui.write("Look at me!!!")