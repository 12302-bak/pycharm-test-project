# _*_ coding: utf-8 _*_


""" a test module"""

__author__ = 'Michael Nancy'


import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()


# 当我们在命令行运行__init__模块时，Python 解释器会把一个特殊变量__name__ 置为 __main__
# 而如果在其他地方导入该模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些指定的代码，常见于运行测试


"""
作用域
"""
# 在模块内部使用的函数或者变量，通过`_`前缀来实现
# 正常的函数或者变量名时公开的（public），可以直接被引用，比如：`abc`, `x123`, `PI`等
# 类似`__xxx__`这样的变量时特殊变量，可以被直接引用，但是有特殊用途，比如上面的`__author__`, `__name__` 就是特殊变量，以及模块定义的文档注释使用的特殊变量`__doc__`
# 我们自己一般不要定义这种变量。
# 类似`_xxx`, `__xxx`这样的函数或者变量就是非公开的（private），不应该直接被引用，比如`_abc`, `__abc` 等。
# 私有变量是不应该直接被引用，而不是不能被直接引用。封装模块细节，
# 一个封装函数的例子


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


"""
模块安装
"""
# 在python中，安装第三方模块，是通过包管理工具pip
# pip install Pillow


"""
安装常用模块
"""
# 在python中一般用到很多第三方库，比如，Pillow，Mysql驱动程序，Web框架Flask，科学计算Numpy等。用pip安装费时费力，还要考虑兼容性。
# 推荐直接安装anaconda，数十个第三方模块自动安装。
# 从Anaconda官网下载GUI（500～600M）安装后，Anaconda会自动把系统path中的python指向自己带的python，并且安装的第三方模块会安装在自己的包路径下面，不影响已安装python目录


"""
    模块搜索路径
"""
# 默认情况下，Python解释器会搜索当前目录，所有已安装的内置模块和第三方模块，搜索路径存放在sys模块 和 path变量中

for v in sys.path:
    print(v)


# 如果我们要添加自己的搜索路径，有两种方法
# 一： 修改sys.path 运行时修改，运行结束后失效
sys.path.append('/Users/path-to-path')
# 二： 设置环境变量'PYTHONPATH'，会自动添加到搜索模块中

