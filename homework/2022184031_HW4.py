import random

def set_students_info():
    global students
    num = 1
    for s in students:
        s['num'] = num
        s['KOR'] = random.randint(0, 100)
        s['ENG'] = random.randint(0, 100)
        s['MATH'] = random.randint(0, 100)
        s['AVG'] = round((s['KOR'] + s['ENG'] + s['MATH'])/3, 2)
        num += 1

def calculate_AVG():
    AVG = [0, 0, 0]
    for s in students:
        AVG[0] += s['KOR']
        AVG[1] += s['ENG']
        AVG[2] += s['MATH']
    AVG[0] = round(AVG[0]/20, 2)
    AVG[1] = round(AVG[1]/20, 2)
    AVG[2] = round(AVG[2]/20, 2)
    return AVG

def show_students_info():
    print('==================================================')
    print('Student    KOR         ENG        MATH        AVG')
    print('--------------------------------------------------')
    for s in students:
        for v in s.values():
            if v == s['num']:
                print("{:>2}".format(v), end='')
            else:
                print("{:>12}".format(v), end='')
        print()
    print('--------------------------------------------------')
    print(f'AVG      {AVG[0]}       {AVG[1]}       {AVG[2]}')
    print('==================================================')

students = [{'num': 0, 'KOR': 0, 'ENG': 0, 'MATH': 0, 'AVG': 0} for i in range(20)]

set_students_info()
AVG = calculate_AVG()
show_students_info()