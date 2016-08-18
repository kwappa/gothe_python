def dump_item(kargs):
    for key, value in kargs.items():
        print(key + ' -> ' + str(value))

dict_var = dict(
    price = 1000,
    name  = '靴下',
    stock = 50,
    code  = 'CY001',
)

dump_item(dict_var)
