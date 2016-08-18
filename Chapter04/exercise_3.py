import random

def make_random_array(elements) :
    result = []
    for i in range(0, elements) :
        result.append(random.randint(0, 100))
    return result

print(make_random_array(10))
