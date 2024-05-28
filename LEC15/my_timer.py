import threading
import datetime
import time

prev_callback_time = datetime.datetime.now()


def callback():
    global prev_callback_time

    # print('작업수행')

    now = datetime.datetime.now()
    delta = now - prev_callback_time
    prev_callback_time = now
    print(f'callback @{now} ({delta})')


looping = True


def simple_timer():
    prev_now = time.perf_counter_ns()
    while looping:
        now = time.perf_counter_ns()
        delay_ns = now - prev_now
        if delay_ns >= 1000000000:
            callback()
            prev_now = now - delay_ns + 1000000000


thread = threading.Thread(target=simple_timer)
thread.start()