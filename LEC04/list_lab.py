[1, 2, 3]
['cat', 'bat', 'rat', 'elephant']
['hello', '3.1415', True, None, 42]

black_pink = ['jisu', 'jeni', 'rose', 'risa']
black_pink[0]
# index error
#black_pink[4]
# 인덱스로 음수 사용 가능.
black_pink[-1]

# [start:stop:step]
# 슬라이스로 리스트를 잘라내면 자료형이 유지가 됨.
num = '0123456789ABCDEF'
num[0:5]
num[1:9:2]
num[ : : ]
num[ : : -1]
black_pink[ : : -1]
type(black_pink)

len(black_pink)
black_pink[0] = 'daehyun'
# 멤버 추가.
black_pink.append('JYP')
# 리스트 더하기.
black_pink += ['YG']

twice = ['momo', 'sana', 'zwi']

unite = black_pink + twice
unite.remove('daehyun')
# 인덱스를 이용해 제거.
del unite[-1]
unite.insert(2, 'IU')

for member in black_pink:
    print(member)

# 파이썬에서는 사용 금지.
#for i in range(len(black_pink)):
#    print(i, member[i])

# 인덱스와 값 같이 꺼내기: enumerate 사용.
for i, member in enumerate(black_pink):
    print(f'{i+1}th member is {member}')

# 코테에서 파이썬 쓰는 거 추천.

'risa' in black_pink
'tom' not in black_pink
'jeni' not in black_pink

# 인덱스를 알 수 있음.
black_pink.index('rose')

# sort
data = [2, 5, 3.14, 1, -7]
data.sort()
# 반대로 정렬.
data.sort(reverse=True)
# 자료형이 다르면 값을 비교할 수 없다.
data.append('cat')
data.sort()

data = ['top', 'four', 'start', 'a']
data.sort()
# key라는 함수를 이용해서 정렬 방법 변경: 문자열 길이를 기준으로 정렬.
data.sort(key=lambda x: len(x))

# 값을 먼저 쓰고 if문을 사용하는 방법.
data = [2, 5, 3.14, 1, -7, 'cat']
data.sort(key=lambda x: x if type(x) in [int, float] else -9999999999999999999999999999)

data = ['top', 'four', 'start', 'a', 2, 5, 3.14, 1, -7, 'cat']
data.sort(key=lambda x: x if type(x) in [int, float] else -9999999999999999999999999999 + len(x))

# 얕은 복사가 되어 안쪽 리스트는 여전히 레퍼런스임.
data1 = [['jisu', 'rose'], [23, 24]]
data2 = data1 # same id
data2 = data1.copy()
data2[0][1] = 'jeni'
print(id(data1[0]))
print(id(data2[0]))

# 깊은 복사, 안쪽 리스트도 제대로 복사가 됨.
import copy
data1 = [['jisu', 'rose'], [23, 24]]
data2 = copy.deepcopy(data1)
data2[0][1] = 'jeni'
print(id(data1[0]))
print(id(data2[0]))

values = [i for i in range(10)]
values = [i for i in range(10) if i%2==1]
# [1,2,3] ['a','b','c']
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b', 'c']]

# 이중 리스트 펼치기.
vec = [[1,2,3], [4,5,6], [7,8,9]]
flattend = [n for v in vec for n in v]

