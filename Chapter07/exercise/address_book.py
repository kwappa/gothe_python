class AddressBook:
    person_list = []            # 登録された人の一覧

    def add(self, person):      # アドレス帳に人を追加
        self.person_list.append(person)

    def show_all(self):         # 登録された人の一覧を表示
        for person in self. person_list:
            print(person.lastname + ' ' + person.firstname)

    def search(self, keyword):  # 検索条件にマッチする登録された人を表示
        for person in self.person_list:
            if keyword in person.firstname or keyword in person.lastname:
                print(person.lastname + ' ' + person.firstname)

    def import_data(self, file):
        import csv
        import datetime

        with open(file, 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # ヘッダーを読み飛ばす

            for row in reader:
                p = Person()
                p.lastname     = row[0]
                p.firstname    = row[1]
                p.mail_address = row[2]
                p.birthday     = datetime.datetime.strptime(row[3], '%Y/%m/%d')
                p.tel          = row[4]

                self.person_list.append(p)

class Person:
    import datetime

    lastname     = ''           # 名前
    firstname    = ''           # 苗字
    tel          = ''           # 電話番号
    mail_address = ''           # メールアドレス
    birthday     = datetime.datetime(2000, 1, 1) # 生年月日

address_book = AddressBook()

gothe = Person()
gothe.firstname = 'ゆもと'
gothe.lastname  = 'みちたか'
gothe.tel       = '090-1234-5678'
address_book.add(gothe)

john = Person()
john.firstname  = 'John'
john.lastname   = 'Lennon'
john.tel        = '090-1234-0098'
address_book.add(john)

print('== 動作確認 ==')

print('アドレス帳の人数 -> ' + str(len(address_book.person_list)) + ' 人')

print('-- 一覧表示 --')
address_book.show_all()

print('-- 検索 --')
address_book.search('John')
