import datetime
import time
import timeit
import random


def calc():
    global result
    result = 0
    for i in range(1, 101):
        result += i


# start_time = time.time()
# for i in range(1000):
#     calc()
# end_time = time.time()
# duration = end_time - start_time
# print(f'{duration=} : {start_time=} {end_time=}')
#
#
# t = timeit.timeit(calc)
# print(t)


# 퀵 정렬 함수
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 버블 정렬 함수
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 랜덤한 정수 리스트 생성 함수
def generate_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

# 정렬 속도 비교 함수
def compare_sorting_algorithms(size):
    # 랜덤 리스트 생성
    random_list = generate_random_list(size, 0, 1000)

    # 퀵 정렬 시간 측정
    quick_sort(random_list)
    quick_sort_time = timeit.timeit(calc)

    # 버블 정렬 시간 측정
    bubble_sort(random_list)
    bubble_sort_time = timeit.timeit(calc)

    # 결과 출력
    print(f"퀵 정렬 시간: {quick_sort_time} 초")
    print(f"버블 정렬 시간: {bubble_sort_time} 초")

# 정렬 속도 비교 실행
#compare_sorting_algorithms(100)

import winsound
target_time = datetime.datetime.now().replace(minute=57, second=0, microsecond=0)
while datetime.datetime.now() < target_time:
    pass
winsound.Beep(440, 1000)