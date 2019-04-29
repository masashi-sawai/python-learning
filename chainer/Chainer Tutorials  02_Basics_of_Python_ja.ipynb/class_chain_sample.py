class Link:

    def __init__(self):
        self.a = 1
        self.b = 2


class Chain(Link):

    def __init__(self):
        # 親クラスの `__init__()` メソッドを呼び出す
        super().__init__()

        # self.c を新たに追加
        self.c = 5

    def sum(self):
        return self.a + self.b + self.c

# インスタンス化
c = Chain()
