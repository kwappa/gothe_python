def compare_string(a, b) :
    if len(a) > len(b) :
        return a
    return b

result = compare_string('this_is_the_longer_string', 'short_string')
print(result)
