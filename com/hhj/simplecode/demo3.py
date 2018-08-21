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



f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
product(5, 6, 7, 9)
trim("   123  ")
