import random

my_hit_point = 15               # 自分のヒットポイント
slime_hit_point = 8             # スライムのヒットポイント
index = 0                       # こうげきの順番（ここでは勇者から）

# どちらかのヒットポイントが0になるまで戦う
while slime_hit_point > 0 and my_hit_point > 0 :
    attack = random.randint(1, 7) # ランダムに与えるダメージを決定
    if index % 2 == 0 :           # 自分の攻撃
        print('スライムに ' + str(attack) + ' のダメージ')
        slime_hit_point -= attack
    else :                      # スライムの攻撃
        print('ゆうしゃに ' + str(attack) + ' のダメージ')
        my_hit_point -= attack
    index += 1

# どちらかが死んでいる
if my_hit_point > 0 :           # 自分のヒットポイントが残っていれば勝ち
    print('スライムをやっつけた')
else :
    print('ゆうしゃは死んでしまった')
