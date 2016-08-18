def test(idx):
    abc = ['a', 'b', 'c']
    try:
        print(abc[idx])
    except IndexError as ie:
        print('インデックスが範囲外となっています。')

test(1)

test(10)
