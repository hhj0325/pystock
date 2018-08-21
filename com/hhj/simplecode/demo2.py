import math


def my_abs(x):
    if x >= 0:
        pass
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def power(z, p=2):
    return z**p


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


print(my_abs(11))
print(my_abs(ord('A')))

m, n = move(100, 100, 60, math.pi / 6)
print("x = %s, y = %s" % (m, n))

r = move(100, 100, 60, math.pi / 6)
print("r = (%s, %s)" % r)

print(power(3, 2))
print(power(3))
print(power(3, 4))
enroll("HH", "M", city="WuHan")
print(calc(1, 2, 3, 4))
print(calc(*(1, 2, 3, 4)))
print(calc(*[1, 2, 3, 4]))

person('Adam', 45, gender='M', job='Engineer')
person('Bob', 35, city='Beijing')




