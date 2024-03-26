test_string = '''
Python is a high-level, general-purpose programming language.
python

나는 아빠도 좋고 엄마도 좋다.
성적은 수, 우, 미, 양, 가로 부여된다.

World is world.

0x3fac
The cat in the hat sat on the flat mat.
참치 꽁치 쥐치 가물치

전화번호 : (010) 1234 5678

12345678 1234-5678

hahahahaha

<이대현> 님 입장하셨습니다>.
final.

djwjod@naver.com
djwjod@tukore.ac.kr
ldh6759@gmail.com
'''

import re

p = re.compile(r'([a-zA-Z]]+)(at)')
# 모두 찾기.
p.findall(test_string)





