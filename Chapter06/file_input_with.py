try:
    with open('test.txt', 'r') as f:
        print(f.read())
except FileNotFoundError as fne:
    print(fne)
