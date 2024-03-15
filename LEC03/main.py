# print에는 기본적으로 개행이 들어가 있음.
# 개행을 END로 변경
import random

print('hello', end='END')
print('world')

# print에서 이어서 작성할 경우 기본적으로 스페이스가 포함이 됨.
# 스페이스를 ,스페이스로 변경
print('cats', 'dogs', 'mice', sep=', ')

# 가변 인자.
# *valuse: 여러 개의 파라미터가 올 수 있다는 뜻.
# 튜플로 들어감.
# 튜플: 리스트와 같지만 넣은 값을 변경할 수 없음.
def print_values(*values):
    for v in values:
        print(v)

def add_values(*values):
    result = 0
    for v in values:
        result += v
    return result

print_values(1, 2)
print_values(1, 2, 3, 4, 5, 6, 'Lee', 3.85)
add_values(1, 2)
add_values(1, 2, 3, 4, 5)

# 가변 키워드 인자.
# **kwargs의 타입은 딕셔너리.
def print_values(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}:{v}")

print_values(name = 'Lim', age = 20, address='Inchen')

# stack은 함수가 호출될 때 함수만 사용할 수 있고, 함수가 종료되면 사라지는 공간.
# heap은 프로그램이 종료될 때까지 자유롭게 사용할 수 있는 공간.

def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bacon'
    print(eggs)

def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)
bacon()
ham()

# 파이썬이 여러 개의 값을 리턴할 수 있는 이유는 튜플을 리턴하기 때문이다.
# _ 사용 시 받고 싶지 않은 값은 받지 않을 수 있음.