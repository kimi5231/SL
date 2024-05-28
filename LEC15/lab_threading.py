import threading


def calc(number=100**4, show='*'):
    global looping
    looping = True
    total_sum = 0
    for i in range(1, number+1):
        if i % (number//10) == 0:
            print(f'{show*3}{i//(number//10)}', end='')
        total_sum += i
    print('\nCalculation Finished.')
    print(f'{total_sum=}')
    looping = False


# thread = threading.Thread(target=calc)
# thread.start()
# print(f'Calculating Starter, but {looping=}.')

thread1 = threading.Thread(target=calc, args=[10**7])
thread1.start()

thread2 = threading.Thread(target=calc, args=[10**6, '+'])
thread2.start()

thread3 = threading.Thread(target=calc, kwargs={'number':10**6, 'show':'='})
thread3.start()