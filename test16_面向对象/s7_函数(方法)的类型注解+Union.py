"""
    在编写函数(方法)时，使用形参data的时候，工具没有任何提示
    在调用函数(方法)时，传入参数的时候，工具无法提示参数类型

    1.所以需要在定义函数方法时，对形参进行注解
def 函数方法名(形参名:类型, 形参名:类型, ...): pass

    2.同时，函数(方法)的返回值也可以添加类型注解
def 函数方法名(形参名:类型, 形参名:类型, ...) -> 返回值类型: pass
"""

# 形参的类型注解
def add(x: int, y: int):  return x + y      # 写入类型注解
add(1, 2)        # ctrl + p 会出现类型提示

# 返回值的类型注解
def func(data: list) -> list:
    return data
print(func([1, 2, 3]))





""" 定义联合类型注解用：from typing import Union
    Union[类型, 类型, ...]
"""
from typing import Union

my_list : list[Union[int, str]] = [1, 2, "zzk"]
my_dict : dict[str, Union[str, int]] = {"name" : "周杰伦", "age" : 18}

def func1(data: Union[int, str]) -> Union[int, str]: pass
func1("zzk")