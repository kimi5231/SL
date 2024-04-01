import re

# 문자열 검색.
p = re.compile('Hello')
text = 'Hello, world and world.'
p.search(text)
p = re.compile('World')

text = '1234-5678'
# 의미를 부여하고 싶은 부분은 괄호로 감쌈. -> 그룹
p = re.compile(r'(\d{4})-(\d{4})')
mo = p.search(text)
mo.group(1)
mo.group(2)
# 전체 그룹.
mo.group()
# 튜플로 넘어옴.
mo.groups()
station_no, user_no = mo.groups()

# Greedy
test_string = 'HaHaHaHaHa'
p = re.compile(r'(Ha){3,5}')
p.search(test_string)
# Non-Greedy
p = re.compile(r'(Ha){3,5}?')
p.search(test_string)

# ^ - 문자열의 시작을 매칭, $ - 문자열의 마지막을 매칭.
p = re.compile(r'^hello')
p.search('hello world')
p.search('She say hello')

p = re.compile(r'\d$')
p.search('you number is 42')
p.search('you number is 42 and my number is ...')

p = re.compile(r'^\d+$')
p.search('1234')
p.search('number is 1234')

# 모든 문자열 매칭.
text = '성: 임   이름: 수영'
p = re.compile(r'성:(.*) 이름:(.*)')
mo = p.search(text)
mo.groups()

# new line /n 매칭.
text = '''This
is
multiple
lines
'''

p = re.compile('.*')
p.search(text)
p = re.compile('.*', re.DOTALL)
p.search(text)

# 대소문자 무시.
p = re.compile(r'hello', re.I)
p.search('HELLO WORLD').group()
p.search('Hello World').group()

# 문자열 교체.
p = re.compile(r'<(\D)\D+>')
p.search('제1회 복권 당첨자는 <임수영>입니다.')
p.sub('***', '제1회 복권 당첨자는 <임수영>입니다.')
p.sub(r'\1**', '제1회 복권 당첨자는 <임수영>입니다.')

# 복잡한 정규식의 쉬운 표시 방법 - VERBOSE.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    \d{3}
    (\s|-|\.)
    \d{4}
    (\s*(ext|x|ext.)\s*\d{2,5})?
    )''', re.VERBOSE)

# 옵션 동시 선택.
someRegexValue = re.compile('foo', re.IGNORECASE| re.DOTALL | re.VERBOSE)