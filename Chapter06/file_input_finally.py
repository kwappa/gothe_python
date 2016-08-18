f = None

try:
    f = open('file_not_found_exception', 'r')
    f.write()
except FileNotFoundError as foe:
    print('ファイルが見つかりませんでした。')
finally:
    if f:
        f.close()
