import random

def get_sum(**kargs):
    result = 0
    for v in range(int(kargs['start']), int(kargs['end']) + 1):
        result += v
    return result

sum = get_sum(start = 1, end = 10)
print(sum)
