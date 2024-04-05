import os
# 경로 지정.
os.chdir(r'C:\Programming\SL\LEC08')
# 바뀐 폴더를 알려줌.
os.getcwd()

# 쓰기 모드로 파일 열기. (파일이 없을 시에는 생성.)
f = open('sample.txt', 'w')
# 파일 쓰기. (기존에 있는 것들을 무시하고 씀.)
f.write('Hello, new world.')
# 파일 닫기.
f.close()

# 붙여쓰기 모드로 파일을 열기, with 사용 시 파일을 닫을 필요가 없음.
with open('sample.txt', 'a', newline='\n') as f:
    f.write('This is Python\n')
    f.write('I Love Python\n')

# 읽기 모드로 파일 열기.
with open('sample.txt', 'r') as f:
    # read는 모두 읽어 들임.
    data = f.read()
    print(type(data))
    print(data)

# 한줄씩 읽기. 더 이상 읽을 내용이 없으면 null로 들어감.
# 모드를 지정해주지 않으면 r 모드를 기본으로 함.
with open('sample.txt') as f:
    l = f.readline(); print(l, end='')
    l = f.readline(); print(l, end='')
    l = f.readline(); print(l, end='')
    l = f.readline(); print(l, end='')
    l = f.readline(); print(l, end='')
    l = f.readline(); print(l, end='')
    l = f.readline(); print(l, end='')
    l = f.readline(); print(l, end='')

# 파일 내용을 모두 읽기.
with open('sample.txt') as f:
    for l in f:
        print(l, end='')

# 파이썬에서는 파일 중간에 붙여넣기는 불가능함.
# 따라서 모든 내용을 복사한 뒤 붙이는 수밖에 없음.
with open('sample.txt') as f:
    # 읽어낸 내용을 리스트로 반환.
    lines = f.readlines()

print(lines)

with open('sample.txt', 'w') as f:
    # 리스트 앞에 삽입하기.
    lines.insert(0, "Header".center(20, '=')+'\n')
    # 리스트 뒤에 추가하기.
    lines.append("Footer".center(20, '=')+'\n')
    # 리스트 내용들을 파일에 쓰기.
    f.writelines(lines)

# 바이너리 쓰기 모드로 열기.
with open('binary.dat', 'wb') as f:
    # 이진 데이터
    f.write(b'0123456789abcdefg')

# 바이너리 읽기 모드로 열기.
with open('binary.dat', 'rb') as f:
    print(f.read(1))
    # 한 번 읽으면, 그 다음 위치부터 읽음.
    print(f.read(1))

f = open('binary.dat', 'rb')
f.read(1)

# 읽고 쓰기 모드로 열기.
f = open('binary.dat', 'rb+')
# 특정 위치로 이동.
f.seek(10)
# 그 위치에 있는 데이터를 변경.
f.write(b'A')
# 맨 처음으로 이동.
f.seek(0)
# 파일 읽기.
f.read()
f.seek(12)
f.write(b'C')
f.seek(0)
f.read()

os.chdir('c:/Windows/System32')
os.getcwd()
# 파일 리스트 생성.
os.listdir()
# 파일 사이즈 확인.
os.path.getsize('calc.exe')
# 파일 생성 시간 확인.
creation_time = os.path.getctime('calc.exe')
# 파일 최종 변경 시간 확인.
modified_time = os.path.getmtime('calc.exe')
# 파일의 마지막 엑세스 시간 확인.
a_time = os.path.getatime('calc.exe')

import time

# 날짜와 시간으로 폼체인지.
time.ctime(creation_time)
time.ctime(modified_time)
time.ctime(a_time)


path = r'd:\work\script\test.py'
# 파일만 보여줌.
os.path.basename(path)
# 경로만 보여줌.
os.path.dirname(path)
# 경로와 파일 분리.
os.path.split(path)
# 확장자 분리.
os.path.splitext(path)

# 현재 경로 확인.
os.getcwd()
# 현재 폴더의 절대 경로 확인.
os.path.abspath('.')
# 상위 폴더의 절대 경로 확인.
os.path.abspath('..')
os.path.abspath('../..')

# 폴더 만들기. (단일 폴더만 생성 가능.)
os.mkdir('temp')
# 임의의 경로에 폴더 만들기.
os.makedirs(r'test/test')

# 원하는 경로에 폴더 생성.
os.chdir(r'c:/')
os.makedirs('myfolder')
# 시스템 폴더에는 생성할 수 없음.
os.makedirs('Windows/myfolder')


import os
os.chdir(r'C:\Programming\SL\LEC08\test')
# 지정된 폴더에 있는 정보를 출력.
for root, subfolders, files in os.walk(r'.\Python'):
    print('info'.center(40, '='))
    print(f'{root=}')
    print(f'{subfolders=}')
    print(f'{files=}')

os.chdir(r'C:\Programming\SL\LEC08\test\Python')
import shutil
# 파일 복사.
shutil.copy('NEWS.txt', 'NEWS2.txt')
# 폴더 복사.
shutil.copytree('Doc', 'Doc2')
# 파일 이름 변경.
shutil.move('python3.dll', 'python4.dll')
# 폴더 이름 변경.
shutil.move('Doc2', 'Doc3')

# 파일 삭제.
os.unlink('NEWS2.txt')
os.remove('NEWS.txt')
# 폴더 삭제.
# rmdir을 사용하면, 폴더를 삭제하기 위해선 안에 파일이 없어야 함.
os.rmdir('tcl')
# rmtree를 사용하면, 내부 파일 유무와 상관없이 삭제할 수 있음.
shutil.rmtree('tcl')

os.chdir(r'C:\Programming\SL\LEC08\test\Python')
import send2trash
# 휴지통으로 보내기.
send2trash.send2trash('python.exe')

os.chdir(r'C:\Programming\SL\LEC08\test\Python')
import winshell
# 휴지통으로 보내기.
winshell.delete_file('python4.dll')
# 휴지통에서 파일 복구하기.
for item in winshell.recycle_bin():
    item.undelete()
# .exe 파일만 복구가 제대로 안됨.
winshell.delete_file('pythonw.exe')
winshell.delete_file('python311.dll')

# 휴지통 파일 내용 확인.
for item in winshell.recycle_bin():
    print(item.real_filename(), item.original_filename(), item.attributes())

import zipfile
# .zip 파일 열기.
zf = zipfile.ZipFile('include_test.zip')
# .zip 파일 내용 보기.
zf.namelist()
# .zip 파일 내에 있는 파일 정보 확인.
zf.getinfo('include/abstract.h')
# 특정 파일 압축 해제.
zf.extract('include/abstract.h')
# .zip 파일 생성.
zf = zipfile.ZipFile('new.zip', 'w')
# .zip 파일에 파일 추가.
zf.write('python4.dll', compress_type=zipfile.ZIP_DEFLATED)
# .zip 파일 닫기.
zf.close()
# 기존 .zip 파일 열기.
zf = zipfile.ZipFile('new.zip', 'a')
# .zip 파일에 파일 추가.
zf.write('python311.dll')
zf.close()

# 리스트 정렬.
a = [1,2,3,4]
a.sort()
# 딕셔너리 정렬.
import random
a = {random.randint(1, 100):'TEST' for _ in range(10)}
sorted(a)
# 딕셔너리 정렬 시, 람다를 이용해 정렬 기준을 설정 후 정렬.
data = {'jisu':165, 'momo':167, 'iu':160}
# 오름차순.
sorted(data.items(), key=lambda x:x[1])
# 내림차순.
sorted(data.items(), key=lambda x:x[1], reverse=True)