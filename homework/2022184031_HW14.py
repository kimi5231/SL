from tkinter import *
import threading
import datetime
import pytz
import time

prev_callback_time = datetime.datetime.now()

KST = pytz.timezone('Asia/Seoul')
BST = pytz.timezone('Europe/London')
EST = pytz.timezone('America/New_York')


def callback():
    global prev_callback_time

    now_kst = datetime.datetime.now(KST)
    now_bst = datetime.datetime.now(BST)
    now_est = datetime.datetime.now(EST)

    kst_label.config(text=now_kst.strftime('KTS: %Y/%m/%d %H:%M:%S'))
    bst_label.config(text=now_bst.strftime('BTS: %Y/%m/%d %H:%M:%S'))
    est_label.config(text=now_est.strftime('ETS: %Y/%m/%d %H:%M:%S'))

    now = datetime.datetime.now()
    delta = now - prev_callback_time
    prev_callback_time = now


def simple_timer():
    prev_now = time.perf_counter_ns()
    while looping:
        now = time.perf_counter_ns()
        delay_ns = now - prev_now
        if delay_ns >= 1000000000:
            callback()
            prev_now = now - delay_ns + 1000000000


def stop(event=None):
    window.quit()
    global looping
    looping = False


window = Tk()
window.title("Time")
window.geometry("320x240+0+0")
window.resizable(False, False)
window.bind("<Escape>", stop)

kst_label = Label(window, text="KST")
kst_label.pack()
bst_label = Label(window, text="BST")
bst_label.pack()
est_label = Label(window, text="EST")
est_label.pack()

looping = True

thread = threading.Thread(target=simple_timer)
thread.start()

window.mainloop()