# _*_  coding: utf-8 _*_

"""
print（）
"""
print('hello,world')

print('hello,world', 'xhsgg12302@126.com')

"""
input()
"""
# name = input('please enter your name:')
# color = input()

# print(name, ': you favorite color is ', color)


print(100 + 200)
print(3.91 * 3.2)
print(10/3)
print(10 // 3)  # 地板除
print(10 % 3)

print(r'''hello,\n world''')

"""
boolean
"""
print(3 < 2)
print(2 > 1)
print(True and True)
print(False and False)
print(True or False)
print(not True)

"""
if else
"""
age = 10
if age >= 18:
    print('adult')
else:
    print('teenager')


"""
coding
"""
print('中文')
print('\u4e2d\u6587')
print('ABC'.encode("utf-8"))
print('中文'.encode('utf-8'))
x = b'\xe4\xb8\xad\xe6\x96\x87'
print(x.decode('utf-8'))
c = b'\xe4\xb8\xad\xe6\x96\xff'
print(c.decode('utf-8', errors='ignore'))
print(len("ABC"))
print('ABC'.__len__())
print(len(b'asd'))
print(len('中文'))
print(len('中文'.encode('utf-8')))


"""
格式化
在python中，采用的格式化方法和C语言是一致的，用%实现 %d, %f, %s, %x
"""
print('Hello, %s' % 'world')
print('Hello, %s ,%s' % ('world', 'xhsgg12302@126.com'))
print('%-4d - %02d + %02d' % (2, 1, 11))
print('%.4f' % 3.1415926)  # 会四舍五入
print('growth rate: %d %%' % 7)  # 需要转义的话用两个%% 表示
"""
格式化二
"""
print('Hello , {0}, 成绩提升了 {1:.1f} %'.format('小明', 17.125))


"""
list 是一种有序集合，可以随时添加和删除其中的元素，数据类型可以不同
"""
classmates = ['Michael', 'Bob', 'Tracy']
complex_list = ['Michael', 'Bob', ['wt', 'site', 'xhsgg12302@126.com'], 'Tracy']
print(classmates)
print(len(classmates))
print(len(complex_list))
print(classmates[1])  # 也会出现list越界
print(classmates[-3])  # 获取倒数第二个
classmates.append('Administrator')  # append方法返回None
# append(),insert(pos,element),pop,pop(pos)


"""
tuple 另一种有序列表：tuple。特性，不可变，不可更改 ,用圆括号 来表示 () 在定义变量的时候就需要初始化
"""
teachers = ('Michael', 'Bob', 'Tracy')
# 可以正常取值，但是并不能改变数据了。
# 定义一个元素的tuple，如果x = (1),这样的话并不是元组这儿按照数学公式中的小括号计算了，所以应该   x = (1,)
t2 = (1,)
t3 = (1, )  # 和t2没有区别
print(len(t2))
print(len(t3))
# 可变的tuple 元素中有一个元素是list的这个可以更改
t4 = ('a', 'b', ['A', 'B'])
t4[2][0] = 'X'
t4[2][1] = 'Y'
print(t4)


"""
条件判断 if else
"""
# condition 1
age = 10
if age >= 18:
    print('adult')

# condition 2

if age >= 18:
    print('adult')
else:
    print('teenager')

# condition 3
if age >= 18:
    print('adult')
elif age >= 16:
    print('teenager')
else:
    print('kid')

# if x: 只要 x 为非零数值，非空字符串，非空list等，就判断为True，否则为False
# input() 返回str,如果要和整数进行比较的话，就需要用 方法 int() 进行转换，但是 int() 如果转换非数字类型的会报错。

print()
"""
循环
for(),while()
"""
# for()
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

rst = 0
for x in (1, 2, 3, 4, 5, 6, 7, 8, 9):
    rst += x
print(rst)

print(range(5))
print(list(range(5)))
for x in range(5):
    print(x, end='\t')  # 根据函数说明猜到如何打印不换行 ^_^
print()

# while()
while_rst = 0
while_n = 99
while while_n > 0:
    while_rst += while_n
    while_n -= 2
print(while_rst)

# break,continue ignore...

"""
dict and set
"""
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Bob'] = 65
d['Bob'] = 45
print(d['Bob'])

# 判断是否存在某个key,不然干取报错
'Thomas' in d  # False

# 还可以通过get()取值 key不存在返回 None ，pop(key) 删除dict中的元素

# 集合
s = set([1, 2, 3])
s.add(4)
s.remove(2)
# 集合可以看作是无序，无重复元素的集合，可以做数学意义伤的交集，并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2  # {2, 3}
s1 | s2  # {1, 2, 3 ,4}

tuple1 = (1, 2, 3)
tuple2 = (1, [2, 3])
d['tuple1'] = tuple1
print(d)
d['tuple1'] = tuple2
print(d)

s.add(tuple1)
# s.add(tuple2)  # tuple2 中的元素规定为不可变元素，但是其中有一个是[2, 3]为list。所以报错
print(s)
print(tuple1)
print(tuple2)
