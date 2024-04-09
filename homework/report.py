import os

os.chdir(r'C:\Programming\SL\LEC08\test')
path = r'C:\Programming\SL\LEC08\test'
for root, subfolders, files in os.walk(r'.\Python'):
    for f in files:
        path = root + '\\' + f
        print(f'{os.path.getsize(f)}'.ljust(10, ' '), end='')
        print(path)