# _*_ coding: utf-8 _*_


# from types import MethodType
from enum import Enum, unique
from all_test.metaclass_test import Model


"""
使用__slots__
"""
# 给实例绑定属性 s.name = 'Michael'
# 给实例绑定方法 s.set_age = MethodType(set_age, s)


def set_age(self, age):
    self.age = age


# 给类绑定方法 Student.set_score = set_score
# 使用__slots__ 可以限制对实例属性的添加

class Student(object):
    __slots__ = ('name', 'age')

# s.score = 99  output: AttributeError: 'Student' object has no attribute 'score'
# 父类的__slots__ 对子类不起作用，除非子类也使用了__slots__,并且，会出现和父类__slots__并集属性


"""
使用@property
"""
# Python内置的@property装饰器就是负责把一个方法变成属性调用的
# @property的实现比较复杂，把一个getter方法变成属性，只需要加上@property.此时这个装饰器本省又创建另一个装饰器@score.setter,负责把一个setter方法变成属性赋值。


class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


# 使用@property后会产生一个@score.setter
# @property函数体中好像除了return，不能又其他语句出现，TabError: inconsistent use of tabs and spaces in indentation
# 使用@property并不是动态生成getter，setter方法，而只是定义一个属性而已。
# 可以只有getter方法，定义只读属性。setter方法，写属性、


"""
多重继承
"""
# 在设计类的继承关系时，通常，主线都是单一继承下来的。例如，Dog继承自Mammal,如果需要混入额外的功能，通过多重继承就可以实现，这种设计通常称之为MixIn.
# 为了更好的看出继承关系，除了主线类外，其他改为混入类型的外观
# 主线类类似Java单继承，混入类类似Java多实现
# 使用多重继承，避免父类出现相同的问题


class Mammal(object):
    pass


class RunnableMixIn(object):
    pass


class CarnivorousMixIn(object):
    pass


class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass


"""
定制类
"""
# 类似 __slots__, __len__ 此类特殊属性或者变量，可以帮助我们定制类
# __str__ : 格式化对象输出，另外还有一个不加print() 调用的 __repr__ ,用于调试，可以如下解决


class Teacher(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Teacher object (name=%s)' % self.name

    __repr__ = __str__

# __iter__:如何想要一个类被用于 for ... in 循环，类似list或tuple那样，就必须实现一个__iter__（）方法。该方法返回一个可迭代对象。
# 然后python 的for循环会调用这个对象的__next__()方法，直到遇到StopIteration错误就退出循环。


class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1 # 出事话两个计数器a, b

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration
        return self.a

# __getitem__:根据下标取元素
# Fib实例虽然能作用域for循环，看起来可list，tuple有点像，但是，把它当作list使用还不行，比如取第5个元素，会报错
# 如下定义可直接取值根据下标


class Fib(object):

    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return

# list有个切片方法


class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# 如果要看成dict ，__getitem__ 的参数也可否能是一个作为key的object，例如str；
# 与值对应的__setitem__方法，把对象是做list或dict来对集合赋值。
# 还有一个__delitem__()方法，用于删除某个元素
# 这些完全归功于python的鸭子类型，不需要强制继承某个接口

# __getattr__()：正常情况下，当我们调用累的方法或者属性时，如果不存在，就会报错
# 要避免这个错误，那就是写一个__getattr__()方法，动态返回一个属性。
# 当调用不存在的属性时，解释器会试图调用__getattr__()来获得属性。我们就有机会返回score的值
# 另外返回函数也是可以的


class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, item):
        if item == 'score':
            return 99  # 返回一个属性
        if item == 'age':
            return lambda: 25   # 返回一个函数


# rest API，利用__getattr__()我们可以写出一个链式调用：
class Chain(object):

    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self.__path, item))

    def __str__(self):
        return self.__path

    __repr__ = __str__

# Chain().status.user.timeline.list
# >>> '/status/user/timeline/list'

# __call__:直接在实例本身上调用。
# 通过callable()函数我们可以判断一个对象是否是'可调用'对象


class Student(object):

    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s.' % self.name)

# s = Student('Michael')
# s() output: My name is Michael.


"""
使用枚举类
"""
# 在没有枚举类的时候，一般通过字典或者类来实现
# 这种方式小心使用没什么问题，但是是可以被修改的
Color = {
    'RED': 1,
    'GREEN': 2,
    'BLUE': 3
}


class Color:
    RED = 1
    GREEN = 2
    BLUE = 3


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 这样我们就获取Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
# 特殊属性__members__是一个将名称映射到成员的有序字典

for month in Month.__members__.items():
    print(month)  # ('Jun', <Month.Jun: 6>)

for name, member in Month.__members__.items():
    print(name, '==>', member, ',', member.value)

# value的属性则是自动赋给成员的`int`常量，默认从`1`开始计数
# 如果要更加精确控制枚举类型，可以从`Enum`派生出自定义类
# @unique 装饰器可以帮助我们检查保证没有重复值。
# 枚举即可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# day1 = Weekday.Mon
# print(day1)               output: Weekday.Mon
# print(Weekday['Tue']      output: Weekday.Tue
# print(Weekday.Tue         output: Weekday.Tue
# print(Weekday.Tue.value)  output: 2
# print(Weekday(1))         output: Weekday.Mon
# print(Weekday(7))         output: ValueError: 7 si not a valid Weekday


"""
使用元类
"""
# type()
# 动态语言和静态语言最大的不同， 就是函数和类的定义，不是编译是定义的，而是运行时动态创建的
# type函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例额，它的类型就是class `Hello`
# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用`type()`函数
# type函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过 class Hello(object)...的定义：
# Hello = type('Hello', (object,), dict(hello=lambda: 40))
# type 构建对象，传入三个参数
#       1. class的名称
#       2。继承的父类集合
#       3。class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
# python解释器遇到class定义时，仅仅是扫面以下class定义的语法，然后调用type()函数创建出class


class Hello(object):

    def hello(self, name='world'):
        print(self.__name__)  # 使用self后，pycharm 就不会出现static 编译警告
        print('Hello, %s' % name)


h = Hello()
print(type(Hello))  # <class 'type'>
print(type(h))      # <class '__main__.Hello'>


# 除了使用type 动态创建类以外，要控制类的创建行为，还可以使用metaclass


class ListMetaclass(type):
    # 1,当前准备创建的类的对象 2，类的名字 3，类继承的父类集合 4，类的方法的集合

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)    # 普通的list没有add方法
print(L)    # output:[1]


# simple ORM example
# outer link
Model()



