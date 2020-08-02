# _*_ coding: utf-8 _*_

import types

"""
类和实例
"""


# 类是创建实例的模版，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响
# 方法就是实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据


class Student(object):  # 类名通常是大写开头的字母，定义类的括号中表示的类是继承类，默认继承object
    pass


bart = Student()
print(bart)  # <__main__.Student object at 0xxx..xxx9>
print(Student)  # <class '__main__.Student'>


# 通过特殊方法`__init__` 绑定认为必要的属性
# 有了__init__ 方法，创建实例的时候必须传入与 __init__方法匹配的参数，并且调用的时候，不必传入 self，Python解释器会自动处理


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score


# 数据封装
# 通过实例方法就可以访问实例的属性，而不必通过外部方法，

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart.print_score()  # output: Bart Simpson: 59

"""
访问限制
"""


# 问题：以上定义的Student类中的数行name,score等属性外部代码可以随意修改?
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线`__`
# 在python中如果实例的变量名以`__`开头，就变成一个私有变量（private），只有内部可以访问，外部不能访问。
# 两对下划线定义的变量名，是特殊变量，可以直接访问。


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


# 改完后，对于外部代码来说，没什么变动， 但是已经无法从外部访问实例变量 `__name`,`__score`
# 两个下划线定义的变量外部直接访问会报错
# 原因是因为私有变量会被python解释器改成_Student__name,所以，仍然可以使用 _Student__name 来访问 __name变量
# 但是不推荐这个做的原因是不同python解释器，这个名字不固定。
# 外部代码获取，怎家get_name,get_score等方法。


"""
继承和多态
"""


# 继承现有的类的类被称为子类，而被继承的称为基类，父类或者超类


class Animal(object):

    def run(self):
        print('Animal is running...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


# 重写父类的方法
class Dog1(Animal):

    def run(self):
        print('Dog is running...')


# 判断一个变量是否是某个类型可以用 `isinstance()` 判断：
# a = list()        isinstance(a, list)     true
# b = Animal()      isinstance(b, Animal)   true
# c = Dog()         isinstance(c, Dog)      true
#                   isinstance(c, Animal)   true    子类继承父类

# 开闭原则： 对扩展开放：允许新增Animal子类，对修改封闭，不需要需改依赖Animal类型的 方法。

# 静态语言 vs 动态语言
# 对于静态语言（like java) 来说，如果需要传入Animal类型，则传入的对象必须是Animal或它的子类，否则，将无法调用run方法
# 对于python这样的动态语言来说，不一定，只要保证传入的对象有一个run方法就可以。 '鸭子类型'，python的'file like object' 就是一种鸭子类型。只要有read方法就可以。


"""
获取对象信息
"""


# type 判断对象类型,返回的是类型
# type(123)     <class 'int'>
# type('123')   <class 'str'>
# type(None)    <type(None) 'NoneType'>
# type(abs)     <class 'builtin_function_or_method'>
# type(a)       <class '__main__.Animal'>


# 判断一个对象是否是函数，使用types中定义的常量


def fn():
    pass


type(fn) == types.FunctionType  # True
type(abs) == types.BuiltinFunctionType  # True
type(lambda x: x) == types.LambdaType  # True
type((x for x in range(10))) == types.GeneratorType  # True


# 使用instance，对于继承关系来说，使用type不方便。
# object -> Animal -> Dog -> Husky
# a = Animal(), d = Dog(), h = Husky()
# isinstance(h, Husky)      output:True
# isinstance(h, Dog)        output:True
# isinstance(h, Animal)     output:True
# isinstance(d, Husky)      output:False

# 使用type可以判断的使用instance也可以判断,总是优先使用isinstance
# 也可以判读是否是其中一种
# isinstance([1, 2, 3], (list,tuple))       output:True
# isinstance((1, 2, 3), (list,tuple))       output:True

# dir可以获取一个对象的所有属性和方法，返回一个包含字符串的list
# dir('ABC')    output: ['__add__', '__class__', ..., '__subclasshook__', 'capitalize', 'casefold', ..., 'zfill']
# 类似__xxx__的属性和方法在python中都是有特殊用途的，比如__len__ 方法返回长度，在python中，如果试图获取一个对象的长度，在len函数内部，它会自动取调用该对象的__len__()方法
# len('ABC') <==> 'ABC'.__len__()


class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
len(dog)    # output: 100

# 配合getattr(),setattr()以及hasattr(),可以直接操作一个对象的状态


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
# hasattr(obj, 'x')     True
# hasattr(obj, 'y')     False
# setattr(obj, 'y', 19)
# hasattr(obj, 'y')     True
# getattr(obj, 'y') == obj.y

# getattr(obj, 'z')     AttributeError: 'MyObject' object has no attribute 'z'
# getattr(obj, 'z', 404)    如果获取不存在的，返回默认值

# 也可以获取一个对象的方法：
# hasattr(obj, 'power')     True
# getattr(obj, 'power')     <bound method MyObject.power of <__main__.MyObject object at 0x...>>


"""
实例属性和类属性
"""
# 给实例绑定属性可以通过 1，self 2,变量名.field=
# 类属性直接在class中定义属性，归类所有；
# 实例属性和类属性如果同名的话，实例会覆盖类属性，删除`del s.name`后又会出现
# 尽量不要对实例属性和类属性使用相同的变量名。否则将产生难以发现的错误。
# 统计学生人数


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        # Student.count += 1
        __class__.count += 1


