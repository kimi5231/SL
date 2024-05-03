import csv

f = open("oscar_age_female.csv")
# 반복자.
reader = csv.DictReader(f, skipinitialspace=True)
for line in reader:
    print(line)
f.close()