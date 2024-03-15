def merge(*str):
    result = ''
    for s in str:
        if s is str[-1]:
            result += 'and ' + s
        else:
            result += s + ', '
    return result

final = merge('orange', 'apple', 'mango', 'banana', 'peanut')
print(final)
print(type(final))