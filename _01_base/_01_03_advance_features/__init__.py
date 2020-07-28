# _*_ coding: utf-8 _*_

"""
切片
"""
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前3个元素： L[0:3] -> ['Michael', 'Sarah', 'Tracy']  *前开后闭
# 从1开始：取两个 L[1:3] -> ['Sarah', 'Tracy']
# 倒数取值： L[-2:] -> ['Bob', 'Jack'], L[-2:-1]-> ['Bob']
# :号 前面没值表示从第一个开始，后面没值表示取到最后一个，什么都不写[:],表示原样取值。
# 出现两个:号表示步长，每几个中取一个 L[:20:2] 表示0～20，每两个元素取一个。
# 'HELLO'[:3] -> 'HEL'


"""
迭代
"""
# 只要是可迭代对象，都可以进行迭代
# dict 默认情况下迭代的是key,如果要迭代value，可以用 for value in d.values(), 如果都需要，则使用 for k, v in d.items().
# 由于字符串也是可迭代对象，因此，也可以用作for循环
# 判断是否可迭代对象，通过collections模块的Iterable类型判断：isinstance([1, 2, 3], Iterable),isinstance('abc', Iterable)
# 若要使用下标，enumerate函数可以把对象变成索引，元素对。for i, value in enumerate(['A', 'B', 'C'])


"""
列表生成式
"""
# 通用写法： [ x * x for x in range(1, 10) ]
# 可以采用两层循环: [ m + n for m in 'ABC' for n in 'XYZ' ]
# if ... else : [ x for x in range(1, 10) if x % 2 == 0 ]  后面的if为筛选条件，不可以加else
# [ x if x % 2 == 0 else -x for x in range(1, 10) ]  前面的if必须加else ，否则无法计算值


"""
生成器
"""
# 通过列表生成式，可以创建一个列表，但是收到内存的限制，列表的容量有限，而且有时候后面的一些元素未必访问，会造成浪费。所以有另外一中边用边生成的解决方式，generator
# 生成器可以使用next() 来取值， 而且本质是可迭代的，所以一般用for循环来取值，不会抛出StopIteration的错误。
# 创建generator，第一种方式很简单，只需要把列表生成式的[]改为(): L = [ x * x for x in range(1, 10)] -> g = ( x * x for x in range(1, 10) )
# 第二种方式可以使用函数实现一个生成器：条件，函数种包含yield关键字。for example:


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


# yield 有两种形式，有括号和无括号，意思和return一样，碰见就返回，调用形式 next(g)
# 以下杨辉三角


def triangles():

    L = [0, 1, 0]
    while True:
        yield [y for y in L if y != 0]
        L = [x if i == 0 else L[i-1] + L[i] for i, x in enumerate(L)] + [0]  # 将append（0） 改为 + 号追加元素


"""
迭代器
"""
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable : isinstance('abc', Iterable)
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator: isinstance(iter([]), Iterator)
# Iterable ---iter()--> Iterator
# range() 并不是一个list，例证：


lis = range(0, 3)
print(lis)
print(isinstance(lis, list))         # False
print(isinstance(list(lis), list))   # True
