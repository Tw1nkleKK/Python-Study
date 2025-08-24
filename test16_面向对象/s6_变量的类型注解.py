""" --只是提示功能--
    类型注解：开发者自身做类型的备注
    类型注解：1.变量的类型注解； 2.函数(方法)的形参和返回值的类型注解
    语法1： 变量: 类型
    语法2： 在注释中， # type: 类型
"""
import json
import random

# 对变量进行类型注解, 一般不写
v1 : int = 10
v2 : bool = False

class Student: pass
stu : Student = Student()

my_list : list = [1,2,3]
my_tuple : tuple = (1,2,3)
my_dict : dict = {'a':1,'b':2,'c':3}

my_list1 : list[int] = [1,2,3]
my_tuple1 : tuple[int,str,bool] = (1,"zzk",False)
my_dict1 : dict[str,int] = {'a':1,'b':2,'c':3}

# 在注释进行类型注解     # type: 类型
var_1 = random.randint(1, 10)   # type: int
var_2 = json.loads('{"name": "zzk"}')   # type: dict[str, str]
