import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# w, h = pyautogui.size()

# pyautogui.moveTo(200,200, duration=1)

# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=1)
#     pyautogui.moveTo(200, 100, duration=1)
#     pyautogui.moveTo(200, 200, duration=1)
#     pyautogui.moveTo(100, 200, duration=1)

pyautogui.mouseInfo()

# pyautogui.click(63, 462)
# pyautogui.doubleClick(143, 456)

# im = pyautogui.screenshot('screen.png')
# im = pyautogui.screenshot('screen.png', region=(0, 0, 100, 100))
# im.show()

# rect = pyautogui.locateOnScreen('1.png')
# p = pyautogui.locateCenterOnScreen('1.png')
# pyautogui.click(p)
# pyautogui.click('2.png')

# all_rects = pyautogui.locateAllOnScreen('2.png')
# for rect in all_rects:
#     pyautogui.click(rect.left+rect.width//2,
#                     rect.top+rect.height//2)

# pyautogui.click(1912,252)
# pyautogui.scroll(-5000)
# pyautogui.scroll(5000)

pyautogui.typewrite('hello from professor\n', 0.25)

import pyperclip

pyperclip.copy('한글은 클리보더로')
pyautogui.hotkey('ctrl', 'v')
pyautogui.typewrite('\n')

pyautogui.drag(100, 0, duration=1)
pyautogui.drag(0, 100, duration=1)
pyautogui.drag(-100, 0, duration=1)
pyautogui.drag(0, -100, duration=1)

pyautogui.dragTo(68, 552, duration=2)
pyautogui.click('send.png')
pyautogui.typewrite('\n')
