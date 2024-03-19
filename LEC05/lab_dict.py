a_student = {'name':'sooyoung', 'grade':'A++'}
type(a_student)
# 'name'이 key.
a_student['name']
a_student['grade']
# age라는 key가 없어 오류 발생.
# a_student['age']

# age:20 추가.
a_student['age'] = 20

# 리스트는 인덱스를 key로 하는 딕셔너리로 볼 수 있음.
# 리스트는 값과 순서가 모두 같아야 같은 리스트임.
# 딕셔너리는 순서 상관 없이 key:value만 같으면 됨.

data = {'color':'red', 'age':42}

# 그냥 data에서 찾으면 key에 대해서만 작동한다.
'color' in data
'red' in data
# value를 확인하고 싶다면 이렇게.
42 in data.values()

# key만 추출.
for k in data.keys():
    print(k)
# value만 추출.
for v in data.values():
    print(v)
# key와 value 모두 추출.
for k, v in data.items():
    print(f'{k=}, {v=}')

# key가 없을 경우, 기본 value 를 대신 선택.
a_student['name']
a_student.get('name')
a_student.get('height', 164)

# 없는 key에 대해 디폴트 값을 지정. 이미 있는 key는 지정되지 않음.
spam = {'name':'Pooka', 'age':5}
spam.setdefault('color', 'black')
spam.setdefault('color', 'white')

text = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for c in text:
    count.setdefault(c, 0)
    count[c] += 1
print(count)

from collections import defaultdict

# lambda: 0 -> 계속 0을 리턴해주는 함수.
# 키가 없을 경우 defaultdict의 lambda 함수가 대신 호출.
count = defaultdict(lambda: 0)
for c in text:
    count[c] += 0
print(count)
print(type(count))

# 집합.
s = {1,2,3}
type(s)
t = {3,4,5}
# 합집합.
s | t
# 교집합.
s & t
# 차집합.
s-t
t-s

s.add(8)
# 순서가 상관이 없음.
{1,2} == {2,1}
