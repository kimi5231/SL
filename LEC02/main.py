#shift + alt + e -> alt + enter
# a는 이름이 아니라 주소다.
a = 1000
id(a)

# result: [2, 3, 4]
# a = b: a와 b는 같은 오브젝트를 가리키게 된다.
# 파이썬은 모든 변수가 레퍼런스다.
# 리스트 안에 리스트가 있을 경우 깊은 복사를 해야 제대로 복사가 된다.
# 인터닝.
# while과 if 안에서 int 0, float 0.0, str '' 은 모두 False 로 계산된다.
import random

for i in range(5):
    print(random.randint(1, 10))