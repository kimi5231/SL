import re


# 지역 번호 또는 핸드폰 번호 체크
# 지역 번호에 괄호가 없는 경우
p = re.compile(r'''
    010|02|051|053|032|062|042|052          # 핸드폰 또는 지역번호 괄호가 없는 경우
''', re.VERBOSE)

# 괄호가 있는 경우, 지역번호 또는 핸드폰 번호
p = re.compile(r'''
    \(          # 괄호 자체
        010|02|051|053|032|062|042|052 
    \)          # 닫는 괄호
''', re.VERBOSE)

# 핸드폰, 지역번호 ( 괄호가 있어도 되고, 없어도 되고 )
p = re.compile(r'''
    ^
    (                                                           # group 1
        (                                                       # group 2
            (010|02|051|053|032|031|062|042|052)          # 핸드폰 또는 지역번호 괄호가 없는 경우   # group 3
            |
            \(                                        # 괄호 자체
                (010|02|051|053|032|031|062|042|052)            # group 4
            \)                                        # 닫는 괄호
        )
        [ ]*-?[ ]*              # 중간 대시, 공백, 또는 아예 없거나...
    )?
    ([123456789]\d{2,3})      # 국번 : 0이 아닌 숫자로 시작, 3자리 또는 4자리     # group 5
    [ ]*-?[ ]*              # 중간 대시, 공백, 또는 아예 없거나...
    (\d{4})                   # 개별 번호 : 4자리                             # group 6
    $
''', re.VERBOSE)

p = re.compile(r'''
    ^
    (                                                        
        (                  
            (010|02|051|053|032|031|062|042|052)     
            |
            \(
                (010|02|051|053|032|031|062|042|052)
            \)     
        )
        [ ]*-?[ ]*          
    )?
    ([123456789]\d{2,3})
    [ ]*-?[ ]*
    (\d{4}) 
    $
''', re.VERBOSE)

# 지역번호국번개별번호
# 공백 또는 대시, 또는 아예 없거나...
# 010  -  9788  -  0000

p = re.compile(r'''
    [ ]*-?[ ]*              # 중간 대시, 공백, 또는 아예 없거나...
''', re.VERBOSE)

# 국번
p = re.compile(r'''
    [123456789]\d{2,3}          # 0이 아닌 숫자로 시작, 3자리 또는 4자리
''', re.VERBOSE)

# 개별 번호
p = re.compile(r'''
    \d{4}          # 4자리
''', re.VERBOSE)



#테스트 코드

p.search('010')
p.search('02')
p.search('111')

# 정상적인 번호에 대한 리스트를 만든다.
good_numbers = [
    '3533435', '34239872', '353 3435', '01034243424',
    '(031) - 8041 0123', '(010) - 333 - 4444'
]

# 잘못된 번호에 대한 리스트
bad_numbers = [
    '010333344444', '010-3333-444', '099 - 353 - 3435', '010 - 34 - 34554', '342498765'
]


def test_good_cases(): # 정상적인 번호에 대해서 테스트 하는 코드
    for s in good_numbers:
        mo = p.search(s)
        if not mo:
            print(f'Failed for good numbers {s}')
        else:
            print(s, '-->', end='')
            if mo.group(3):     # 괄호 없는 지역 번호, 핸드폰 번호 존재
                print(f'({mo.group(3)}) - {mo.group(5)} - {mo.group(6)}')
            elif mo.group(4):   #괄호 있는 지역 번호, 핸드폰 번호 존재
                print(f'({mo.group(4)}) - {mo.group(5)} - {mo.group(6)}')
            else:   # 핸드폰 번호로 간주
                print(f'(010) - {mo.group(5)} - {mo.group(6)}')


def test_bad_cases():   # 비정상적인 번호에 대해서 테스트 하는 코드
    for s in bad_numbers:
        mo = p.search(s)
        if mo:
            print(f'Failed for bad numbers {s} : {mo.group()}')
        else:
            print(f'{s} --> Wrong Number')

def test_all():
    test_good_cases()
    test_bad_cases()


test_all()


import exrex


for i in range(100):
    print(exrex.getone(pattern_str, 2)) # 특정 패턴을 갖는 문자열을 랜덤으로 생성...

p.pattern # 원래 정규식의 문자열이 그대로 들어있다.
pattern_str = re.sub(r'[ ]{2,}|\t|\n', '', p.pattern) # 2개 이상의 연속된 공백, 탭, 개행 문자 삭제