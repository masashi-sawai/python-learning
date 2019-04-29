class MyNetwork(Chain):
    
    def mul(self):
        return self.a * self.b * self.c

net = MyNetwork()

net.mul()