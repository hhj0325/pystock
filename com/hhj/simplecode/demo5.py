import functools, time


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1, f2, f3)
print(f1(), f2(), f3())


def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count1()
print(f1, f2, f3)
print(f1(), f2(), f3())


def createCounter():
    a = 0
    def counter():
        nonlocal a
        a = a + 1
        return a
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())

L = list(filter(lambda x : x % 2 ==1, range(20, 40)))
print(L)


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2015-3-25')

now()
print(now.__name__)


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        d1 = time.time()
        func = fn(*args, **kw)
        d2 = time.time()
        print('%s executed in %s ms' % (fn.__name__, d2 - d1))
        return func
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
print(f)
print(s)

int("123456",2)