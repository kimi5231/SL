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
"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""

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
# 모든 알파벳이 소문자인가?
spam.islower()
# 모든 알파벳이 대문자인가?
spam.isupper()

'HELLO'.isupper()
'abc12345'.islower()
'12345'.islower()
'12345'.isupper()

# 뒤에 적힌 문자열로 시작하는가?
'Hello world!'.startswith('Hello')
'abc123'.startswith('abcdef')
# 뒤에 적힌 문자열로 끝나는가?
'Hello world!'.endswith('world!')
'abc123'.endswith('12')

# 앞에 있는 구별 문자열을 이용해 리스트에 있는 문자열들을 합친다.
':'.join(['cat', 'rat', 'bat'])

''.join(str(i) for i in range(20))

# 기준에 따라 문자열을 분리. (모든 공백 space, \n \t \v \f \r)
'my name is sooyoung'.split()
'my name is sooyoung\ni love you'.split()
'my name is sooyoung\ti love you'.split()
'my name is sooyoung i love you'.split('o')
# 줄 단위로 분리.
spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
spam.split('\n')

# 문자열을 separator 문자열을 기준 삼아 세개의 문자열로 분리.
# before, separator, after
'Hello, world!'.partition('w')
'Hello, world!'.partition('world')
'Hello, world!'.partition('XYZ')

# 문자열 정렬.
'hello'.rjust(10)
'hello'.ljust(10)
'hello'.center(10)
'hello'.center(11, '=')

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

# 아스키코드에 따라 문자를 숫자로 변경.
ord('A')
# 아스키코드에 따라 숫자를 문자로 변경.
chr(65)

# pyperclip.
import pyperclip
# 문자열을 클립보드에 저장.
pyperclip.copy('hello, world')
pyperclip.copy(''.join(str(n) for n in range(1000)))
# 클립보드에 있는 내용을 가져옴.
pyperclip.paste()