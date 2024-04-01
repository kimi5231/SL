import keyboard


def write_10numbers():
    keyboard.write(''.join(str(n) for n in range(10)))


keyboard.add_hotkey('shift+windows+w', write_10numbers)
keyboard.wait('esc') # 무한루프 esc 종료
keyboard.remove_all_hotkeys()