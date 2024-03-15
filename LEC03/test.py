import random

# any(), all()
ages = [random.randint(1, 100) for n in range(20)]

if any(i < 18 for i in ages):
    print('미성년자 있음.')
else:
    print('모두 다 성인임.')

print('모두 다 성인임.') if all(i >= 18 for i in ages) else print('미성년자 있음.')

# filter()
numbers = [random.randint(0, 99) for i in range(20)]

def mul3_filter(n):
    return n%3==0
result = list(filter(mul3_filter, numbers))

result = list(filter(lambda n: n % 3 == 0, numbers))

# zip()
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
heights = [180.5, 172.1, 185.3]
zipped = zip(names, ages, heights)
print(list(zipped))