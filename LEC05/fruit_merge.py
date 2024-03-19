def merge(*fruits):
    result = ''
    for fruit in fruits[:-1]:
        result += f'{fruit}, '
    result += ('and ' if result else '') + fruits[-1]
    return result

assert(merge('apple') == 'apple')
assert(merge('apple', 'banana') == 'apple, and banana')
assert(merge('apple', 'banana', 'mango', 'cherry') == 'apple, banana, mango, and cherry')
# print(merge('apple'), '=====', 'apple')
# print(merge('apple', 'banana'), '=====', 'apple, and banana')
# print(merge('apple', 'banana', 'mango', 'cherry'), '=====', 'apple, banana, mango and cherry')