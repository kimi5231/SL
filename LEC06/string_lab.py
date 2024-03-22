# 파이썬은 작은 따옴표로도 문자열을 표현 가능.
spam = "hello"
spam = 'hello'
# 각 따옴표 별로 다른 따옴표로 감싸면 그대로 사용할 수 있음.
stmt = 'hel ""lo   '
stem = "It's good. "

# escape 캐릭터를 무시.
print(r'that is carol\'s cat.')

# Multiple Line.
def print_lines():
    print('''
애국가:
    동해.....
END.
    ''')

print_lines()

# Multiline Comments.
""""""

# 리스트 슬라이스와 동일.
message = 'hello, world'
even_message = message[::2]
even_message

# in 사용 가능
'hel' in 'hello'
'llo' in 'hello'
'' in 'hello'

# 알파벳인가?
'hello'.isalpha()
'hello123'.isalpha()
# 알파벳이나 숫자인가?
'hello123'.isalnum()
'hello'.isalnum()
# 10진수인가?
'123'.isdecimal()
# 공백인가? 개행문자와 같은 특수 문자 포함.
'    '.isspace()
# 첫 글자가 대문자인가?
'This Is Title Case'.istitle()
'This Is Title Case 123'.istitle()
'This Is not Title Case'.istitle()
'This Is NOT Title Case Enter'.istitle()

# 모든 알파벳을 대문자로 변경.
spam = 'Hello world!'
spam = spam.upper()
spam
# 모든 알파벳을 소문자로 변경.
spam = spam.lower()
spam

# 앞에 있는 구별 문자열을 이용해 리스트에 있는 문자열들을 합친다.
':'.join(['cat', 'rat', 'bat'])

''.join(str(i) for i in range(20))

# 기준에 따라 문자열을 분리.
'my name is sooyoung'.split()
'my name is sooyoung\ni love you'.split()
'my name is sooyoung\ti love you'.split()

# 문자열을 separator 문자열을 기준 삼아 세개의 문자열로 분리.

# 문자열 정렬.
'hello'.rjust(10)
'hello'.ljust(10)
'hello'.center(10)
'hello'.center(10, '=')

def print_picnic(food, lwidth, rwidth):
    print('PICNIC FOOD'.center(lwidth+rwidth, '='))
    for k, v in food.items():
        print(k.ljust(lwidth, ' ') + str(v).rjust(rwidth))

food = {'sandwiches':4, 'apple':12, 'cups':4, 'cookies':8000}
print_picnic(food, 12, 5)
print_picnic(food, 20, 6)

# 문자 제거.
spam = ' hello world '
spam.strip()
# 왼쪽에 있는 문자만 제거.
spam.lstrip()
# 오른쪽에 있는 문자만 제거.
spam.rstrip()

spam = 'Hello World!'
# 문자열의 문자가 모두 소문자인가?
spam.islower()
# 문자열의 문자가 모두 대문자인가?
spam.isupper()
'HELLO'.isupper()
'abc12345'.islower()
'12345'.islower()
'12345'.isupper()

# 아스키코드에 따라 문자를 숫자로 변경.
ord('A')
# 아스키코드에 따라 숫자를 문자로 변경.
chr(65)

# pyperclip.
import pyperclip
pyperclip.copy('hello, world')
pyperclip.copy(''.join(str(n) for n in range(1000)))