"""
    1.函数的多返回值
    2.函数的多种传参方式
    3.匿名函数
"""
from tkinter.font import names


# 1.多返回值，类型不受限
def test_return():
    return 1, "hello", True

x, y, z = test_return()
print(x)
print(y)
print(z)


# 2.函数的多种传参方式 ---->  一共四种： (位置参数、关键字参数、不定长参数、缺省参数)
def user_info(name, age, gender):
    print(f"姓名是: {name}, 年龄是: {age}, 性别是: {gender}")
    # ①默认使用 位置参数
user_info("周", 18, "男")
    # ②关键字参数
user_info(name="王", age=11, gender="male")
user_info(age=3, name="吴", gender="female")
user_info("张", gender="female", age=10)

    # ③缺省参数：用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值 [函数定义时默认值必须写在最后面，如下面的gender]
def user_info2(name, age, gender="male"):
    print(f"姓名是: {name}, 年龄是: {age}, 性别是: {gender}")
user_info2('Tom', 18)
user_info2(name="JJ", age=1, gender="female")


    # ④不定长参数：即可变参数，用于调用时不确定会传递多少个参数的情况(不传参也可以)  [位置参数、关键字传递]
        # {元组}  不定长定义的形式参数会作为元组存在，接受不定长的参数传入 --> 一个 * 号
def user_info3(*args):
    print(f"{args}的类型是: {type(args)}, 内容是: {args}")
user_info3('zzk', 18, 'male')
        # {字典}  关键字不定长 --> 两个 * 号 keyword
def user_info4(**kwargs):
    print(f"args的参数类型是: {type(kwargs)}, 内容是: {kwargs}")
user_info4(name="迪迦", age=111, gender="male")