from functools import reduce


def my_upper(my_name):
    return my_name[0].upper() + my_name[1:].lower()


def prod(L):
    def my_sum(x, y):
        return x + y
    return reduce(my_sum, L)


def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]

name = ['adam', 'LISA', 'barT']
print(list(map(my_upper, name)))

L = [3, 5, 7, 9]
print(prod(L))

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)

L2 = sorted(L, key=by_score, reverse=True)
print(L2)


