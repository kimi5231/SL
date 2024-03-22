import keyboard
import pyperclip


def words_count():
    words_list = [w for w in pyperclip.paste().split() if w.isalpha()]
    for w in words_list:
        words.setdefault(w, 0)
        words[w] += 1
    print_words(20, 20)


def print_words(lwidth, rwidth):
    print(' Word Count '.center(lwidth + rwidth, '='))
    for k, v in words.items():
        print(k.ljust(lwidth) + str(v).rjust(rwidth))


words = {}
keyboard.add_hotkey('shift+windows+w', words_count)
keyboard.wait('esc')
keyboard.remove_all_hotkeys()