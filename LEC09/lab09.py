# 예외 처리.
# try:
#     age = int(input("Enter Age:"))
#     if age < 18:
#         raise ValueError('Too young')
# except Exception as err:
#     print(f'{err=}')


import traceback


def f3():
    age = int(input("Enter Age:"))
    if age < 18:
        print('you cannot enter.')


def f2():
    f3()


def f1():
    for i in range(5):
        try:
            f2()
        except Exception as err:
            with open('error.log', 'a') as ef:
                ef.write(traceback.format_exc())


f1()


# 로직에 대한 중간 점검.
data = 100
assert data == 100
assert data < 100, 'data is lower then 100'