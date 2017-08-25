dirty = ['fuck', '狗日的', '犊子', '麻批', '仙人板板', 'R你妈', '操你', '草你']


class Player(object):
    def __init__(self, name):
        self.name = name
        self.string = ''

    def talk(self):
        self.string = 'whatever fuck no 仙人板板 joke'
        self.log()
        for i in dirty:
            self.string = self.string.replace(i, '*')
        print("公屏显示:%s--%s" % (self.name, self.string))

    def log(self):
        print("日志记录为:%s--%s" % (self.name, self.string))

t1 = Player('white')
t1.talk()
