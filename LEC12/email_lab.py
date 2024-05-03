import csv

f = open("simple.csv")
# 반복자.
reader = csv.reader(f, skipinitialspace=True)
for line in reader:
    print(line)
f.close()