import pyautogui
import pyperclip
import time

pyautogui.click(635,220)
pyperclip.copy('오늘의 날씨')
pyautogui.hotkey('ctrl', 'v')
pyautogui.typewrite('\n')
time.sleep(1)

pyautogui.screenshot('날씨.png', region=(127, 366, 1120, 600))

pyautogui.hotkey('win')
pyperclip.copy('카카오톡')
pyautogui.hotkey('ctrl', 'v')
pyautogui.typewrite('\n')
time.sleep(5)

pyautogui.doubleClick(971,434)
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('날씨.png')
pyautogui.hotkey('ctrl', 'v')
pyautogui.typewrite('\n')
pyautogui.typewrite('\n')