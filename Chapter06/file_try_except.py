try:
    file = open('python.txt', 'r')
except FileNotFoundError as foe:
    print('ファイルが見つかりませんでした。確認してください。')
