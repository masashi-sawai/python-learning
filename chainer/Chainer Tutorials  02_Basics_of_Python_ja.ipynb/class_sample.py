# クラスの定義
class House:

    # __init__() の定義
    def __init__(self, name):
        self.name_plate = name

    # メソッドの定義
    def hello(self):
        print('{}の家です。'.format(self.name_plate))

# 呼び出し
sato = House('佐藤')
suzuki = House('スズキ')

sato.hello()   # 実行の際には hello() の引数にある self は無視
suzuki.hello()  # 実行の際には hello() の引数にある self は無視
