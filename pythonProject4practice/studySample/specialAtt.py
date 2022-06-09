class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age

c = C('小明', 20)
# c.__dict__ 实例对象的属性字典
# {'name': '小明', 'age': 20}
print(c.__dict__)
# C.__dict__ 类的属性字典
# {'__module__': '__main__', '__init__': <function C.__init__ at 0x0000023A003FC040>, '__doc__': None}
print(C.__dict__)
# c.__class__ 实例对象的类属性
# <class '__main__.C'>
print(c.__class__)
# C.__class__ 类属性
# <class 'type'>
print(C.__class__)
# C.__bases__ 类的基类集合
# (<class '__main__.A'>, <class '__main__.B'>)
print(C.__bases__)
# C.__base__ 类C的最近得基类
# <class '__main__.A'>
print(C.__base__)