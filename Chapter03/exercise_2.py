for y in range(1, 10) :
    for x in range(1, 10) :
        product = x * y
        if product < 10 :
            product = ' ' + str(product)
        print(str(product), end = '')
        if x < 9 :
            print(' ', end = '')

    print('')
