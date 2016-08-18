def add_number(a, b):
    try:
        return a + b
    except TypeError as te:
        return '数値以外のデータが与えられています。'

print(add_number(2, 2))

print(add_number(3, 'abc'))
