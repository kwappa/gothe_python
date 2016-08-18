def nabeatsu(v) :
    if v % 3 == 0 or '3' in str(v) :
        return 'アホ'
    return v

for v in range(1, 41) :
    print(nabeatsu(v))
