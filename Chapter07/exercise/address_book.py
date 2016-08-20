class AddressBook:
    person_list = []            # 登録された人の一覧

    def add(self, person):      # アドレス帳に人を追加
        pass

    def show_all(self):         # 登録された人の一覧を表示
        pass

    def search(self, keyword):  # 検索条件にマッチする登録された人を表示
        pass

class Person:
    import datetime

    lastname     = ''           # 名前
    firstname    = ''           # 苗字
    tel          = ''           # 電話番号
    mail_address = ''           # メールアドレス
    birthday     = datetime.datetime(2000, 1, 1) # 生年月日
