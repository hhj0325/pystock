import datetime

time = datetime.datetime.now()
speak = '你个狗日的，fuckR你妈哟，操你个大头鬼，个老麻批啊啊啊狗日的巴巴爸爸狗日的'
dirty = ['fuck', '狗日的', '犊子', '麻批', '仙人板板', 'R你妈', '操你', '草你']

for i in dirty:
    speak = speak.replace(i, '*')

now = datetime.datetime.now()
print(speak + " | " + str(now - time))

