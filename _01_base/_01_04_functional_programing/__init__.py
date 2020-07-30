# _*_ coding: utf-8 _*_

import functools, time

"""
高阶函数
"""
# 函数名其实是一个指向函数的变量，即变量可以指向函数 : f = abs , f(-10) //output: 10
# 要让 abs 指向 10 在其他模块也生效，要用 import builtins; builtins.abs = 10;
# 一个函数可以接受另外一个函数作为参数，这种函数就称之为高阶函数


def add(x, y, f):
    return f(x) + f(y)


add(-5, 6, abs)  # output: 11

# map/reduce
# map 函数接受两个参数，一个是函数，一个是Iterable, map 将传入的函数作用于每一个元素，并把结果作为新的Iterator返回。
# for example： def f(x):\n return x * x , r = map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])  -> [1, 4, 9, 16, 25, 36, 49, 64, 81]
# 以上由于返回的r 是 惰性Iterator，使用list()将整个 序列计算并返回。

# reduce 函数接受两个参数，一个函数（必须接受两个参数，将两个数的结果和下一个数继续迭代），一个是Iterable.
# 其效果就是： reduce(f,[x1, x2, x3, x4]) -> f(f(f(x1, x2), x3), x4)
# def fn(x, y): \n return x * 10 + y , r = reduce(fn, [1, 3, 5, 7 ,9]  :output 13579


def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# filter 过滤序列
# 埃式筛选法


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def primes():
    yield 2
    it = _odd_iter()  # 初始化序列
    while True:
        n = next(it)
        yield n
        it = filter(lambda x: x % n > 0, it)


# 判断回文数


def is_palindrome(n):
    if n % 10 == 0:
        return False
    revert_number = 0

    while n > revert_number:
        revert_number = revert_number * 10 + n % 10
        n = int(n / 10)
    return n == revert_number or n == int(revert_number / 10)


# sort 排序
# Python 内置的sorted（）函数可以对list进行排序：sorted([36, 5, -12, 9, -21])
# 此外，sorted也是一个高阶函数，可以接受一个key函数来实现自定义的排序，例如按照绝对值大小排序： sorted([36, 5, -12, 9, -21], key=abs)
# 逆序：sorted([36, 5, -12, 9, -21], key=abs, reverse=True)
# 成绩从高到底可以使用 '-' 号反转

"""
返回函数
"""
# 返回一个函数
# 闭包


def count():  # origin
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


def count1():  # update1
    fs = []
    for i in range(1, 4):
        def f(_i=i):
            return _i*_i
        fs.append(f)
    return fs


def diy_count():    # update2
    fs = []

    def f(c):
        def g():
            return c*c
        return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs


def my_count():     # update 3 think of myself
    _list = []
    for v in range(1, 4):
        def g(x):
            def c():
                return x * x
            return c
        _list.append(g(v))
    return _list


f4, f5, f6 = my_count()
print(f4())
print(f5())
print(f6())


"""
匿名函数
"""
# for example : list(map(lambda x: x * x ,[1, 2, 3, 4, 5, 6]
# 此处匿名函数 lambda x: x * x 实际上就是 def f(x): \n return x * x

"""
装饰器
"""
# 增强一个函数，又不希望修改函数原先的定义，这种在代码运行期间动态增加功能的方式，称之为'装饰器'Decorator
# 本质上，装饰器就是一个返回函数的高阶函数。


def log(func):
    def wrapper(*args, **kw):
        print('包装块')
        return func(*args, **kw)
    return wrapper


def text(text):
    def log(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(text,'包装块')
            return func(*args, **kw)
        # wrapper.__name__ = func.__name__
        return wrapper  # wrapper <==> my_wrap(args)(wrapper) <==> out_wrapper
    return log

# 使用自定义的改名装饰器


def my_wraps(origin):
    def decorator(inner_wrapper):
        def out_wrapper(*args, **kw):
            return inner_wrapper(*args, **kw)
        out_wrapper.__name__ = origin.__name__
        return out_wrapper
    return decorator


def metric(fn):
    # @functools.wraps(fn)
    @my_wraps(fn)
    def wrapper(*args, **kw):
        s = time.time()
        rst = fn(*args, **kw)
        e = time.time()
        print('%s executed in %s ms' % (fn.__name__, e-s))
        return rst
    # wrapper.__name__ = fn.__name__
    return wrapper  # wrapper <==> my_wrap(args)(wrapper) <==> out_wrapper


@metric
def test_name():
    pass


fx = test_name
print(fx.__name__)


"""
偏函数
"""
# functools.partial的作用就是：把一个函数的某些参数给固定住（也即是设置默认值），返回一个新函数。简单调用

int('12345', base=8)
int('12345', 16)


def int2(x, base=2):
    return int(x, base)

# 以上可以使用偏函数一步搞定


int2 = functools.partial(int, base=2)


# 偏函数一旦固定，在调用的时候就不能够再赋值


def fun(a, b, c):
    return a + b + c


f = functools.partial(fun, b=2)
print(f(1, c=3))
# print(f(1, b=4, 3))  放开后有语法错误
print(f(1, 4, 3))
print(f(1, 3))


# max2 = functools.partial(max, 10)
# max2(5, 6, 7) <==> max(10, 5, 6, 7)



