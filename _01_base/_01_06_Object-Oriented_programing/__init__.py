# _*_ coding: utf-8 _*_

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

"""
获取对象信息
"""

"""
实例属性和类属性
"""
