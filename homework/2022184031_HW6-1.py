import re
import exrex


def check_correct_num():
    global p

    phoneNum = p.search(num)
    return phoneNum


def print_error():
    if phoneNum and phoneNum.group(1) == None and len(num) >= 10:
        print('Wrong Local Number')
    else:
        print('Wrong Number')


def change_num_format():
    if phoneNum and phoneNum.group() == num:
        firstNum, secondNum, thirdNum = phoneNum.groups()
        print_phoneNum(firstNum, secondNum, thirdNum)
    else:
        print_error()


def print_phoneNum(firstNum, secondNum, thirdNum):
    if firstNum == None:
        firstNum = '010'
    print(f'({firstNum}) {secondNum} - {thirdNum}')


p = re.compile(r'\(?(010|02|051|053|032|062|042|052|044|031|033|043|041|063|061|054|055|064)?\)? ?-? ?([1-9][0-9]{2,3}) ?-? ?([0-9]{4})')
pattern_str = re.sub(r'[ ]{2,}|\t|\n', '', p.pattern)
for i in range(100):
    num = exrex.getone(pattern_str, 2)
    phoneNum = check_correct_num()
    change_num_format()