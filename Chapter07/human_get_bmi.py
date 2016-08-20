class Human:
    age       = 0               # 年齢
    lastname  = ''              # 名前
    firstname = ''              # 苗字
    height    = 0.0             # 身長
    weight    = 0.0             # 体重

    def get_bmi(self):
        return (self.weight) / (self.height ** 2)

nakata = Human()

nakata.lastname  = '中田'
nakata.firstname = '敦彦'
nakata.weight    = 68
nakata.height    =  1.7

bmi = nakata.get_bmi()
print(bmi)
