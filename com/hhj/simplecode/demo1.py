height = 1.75
weight = 80.5
bmi = weight / height / height
print("%.2f" % bmi)
if bmi < 18.5:
    print("so light")
elif bmi < 25:
    print("normal")
elif bmi < 28:
    print("so weight")
elif bmi < 32:
    print("fat")
else:
    print("so fat")

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("0 hello %s" % name)
    print("1 hello {0}".format(name))

for index in range(len(L)):
    print(index)
    print(L[index])

n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END 1')


n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
print("END 2")
