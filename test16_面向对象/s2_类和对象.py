""" 1.
    现实世界中事物都可以分为：属性 和 行为。
    类 也有属性和行为。
    所以，使用程序的类可以完美的描述现实世界的事物。
"""
from test16_面向对象.s1_初识类 import stu_1


class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,500)

clock1 = Clock()
clock1.id = 1
clock1.price = 9.9
print(f"闹钟ID:{clock1.id}, price:{clock1.price}")
clock1.ring()


""" 2.
    构造方法： python类可以使用 __init__() 方法
    可以实现：
        在创建类对象(构造类)的时候，会自动执行
        在创建类对象(构造类)的时候，将传入参数自动传递给__init__方法使用
"""
class Student11:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Student init")

stu_11 = Student11("周杰伦", 30)
stu_22 = Student11("邓紫棋", 20)


""" 3. 魔术方法
    内置方法： 与__init__相同。
    这些内置的类方法，各自有各自特殊的功能，这些内置方法我们叫做 魔术方法。
                           < >    <= >=     ==             
    __init__ 、 __str__ 、__lt__ 、__le__ 、__eq__
"""

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"People {self.name}, age: {self.age}"

    def __lt__(self, other):        # other 另一个类对象
        return self.age < other.age

    def __le__(self, other): return self.age <= other.age
    def __eq__(self, other): return self.age == other.age

p1 = People("林俊杰", 30)
print(p1)
p2 = People("薛之谦", 30)
print(p2)
print(p1 < p2)
print(p1 <= p2)
print(p1 == p2)     # 没有__eq__的话，结果为False。原因是：==默认对比的是p1和p2的地址



