import csv

f = open("mydata.csv", 'w', newline='')
# 구별자 변경.
writer = csv.writer(f, delimiter=':', quoting=csv.QUOTE_ALL)
writer.writerow([100, 176, 80])
writer.writerow([101, 180, 90])
writer.writerow(['lim, sooyoung', 180, 88])
writer.writerows([
    [1,2,3], [4,5,7]
])
f.close()