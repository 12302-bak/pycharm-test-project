# _*_ coding: utf-8 _*_

import math
from functools import reduce
import time, functools

"""
函数调用
"""
# 可以通过help(abs),查看函数abs帮助信息,max(),int(),str(),float(),bool() ,hex(),函数可以直接赋值
# 类型转换函数：int,float,str,bool。其中可以使用bool函数判断什么样的值为True or False.

"""
定义函数
"""
# 在python 中，定义函数使用def 关键字，函数名（参数列表）+ : ，在缩进块中写函数体，有返回值用return.
# python中不可以出现函数体中为'' 的情况，可以用pass代替。


def my_abx(x):
    if x >= 0:
        return x
    else:
        return -x


# 参数检查
# 可以使用isinstance()函数来检查参数类型、使用raise 抛出异常；


def my_abs(y):
    if not isinstance(y, (int, float)):
        raise TypeError('bad operand type')
    if y >= 0:
        return y
    else:
        return -y


# 返回多个值 ,其实返回的是一个元组，按照位置赋予响应的值
# 如果没有返回值，则自动return None

"""
函数的参数
"""
# 函数的参数分为；位置参数，默认参数，可变参数，关键字参数，命名关键字参数
# 1, 空空空位置参数    def power(x):
# 2, 空空空默认参数    def power(x, n=2):                       存在多个默认参数时，解释器会按照顺序赋值，如果要指定参数赋值，可以写入参数名。
# 3, 空空空可变餐数    def calc(*numbers):                      '*' 可以将tuple 或者 list 组装成多个参数传入到可变参数函数
# 4, 空空关键字参数    def person(name, age, **kw):             '**' 跟'*' 基本一致
# 5, 命名关键字参数    def person(name, age, *, city, job):     当存在可变参数的时候，不用再另外加一个*
# 6, 参数组合，以上可以随意组合，但是必须注意顺序：位置参数，默认参数，可变参数，命名关键字参数，关键字参数。
# 7, def function(*args, **kw)，这种函数可以接受任意传参。


"""
递归函数
"""


def hanoi_move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi_move(n-1, a, c, b)
        print(a, '-->', c)
        hanoi_move(n-1, b, a, c)





