import re

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

text = '성: 임   이름: 수영'
# 모든 문자열 매칭.
p = re.compile(r'성:(.*) 이름:(.*)')
mo = p.search(text)
mo.groups()