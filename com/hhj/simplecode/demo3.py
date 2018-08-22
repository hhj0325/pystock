def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


def product(*x):
    sum = 1
    if len(x) > 0:
        for item in x:
            sum = item * sum
    print(sum)


def trim(s):
    start = 0
    for c in s[:]:
        if(c == ' '):
            start += 1
        else:
            break
    end = -1
    for c in s[-1:]:
        if (c == ' '):
            end += -1
        else:
            break
    print(s[start: end])


def find_min_and_max(L):
    temp_min = L[0]
    temp_max = L[0]
    for x in L:
        if x < temp_min:
            temp_min = x
        if x > temp_max:
            temp_max = x
    print(temp_min, temp_max)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

def triangles(n = 10):
    results = []
    for x in range(n):
        if x == 0:
            results.append([1])
        elif x == 1:
            results.append([1, 1])
        else:
            temp = [1]
            for y in range(x):
                temp.append(results[x-1][y])


def odd():
    n = 1
    for index in range(1, max + 1):
        yield n
        n = n + 2
        print('step = ', index, 'n = ', n)


def add(x, y, f):
    return f(x) + f(y)




f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
product(5, 6, 7, 9)
trim("   123  ")

find_min_and_max([10, 9, 11, 23, 21, 7, 99, 11])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]


list1 = [1,6,2,5,3]
list2 = [34,67,13,678,67]
print(add(list1,list2,max))
