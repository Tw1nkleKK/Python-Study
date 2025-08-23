"""
    模块：就是一个Python文件，里面有类、函数、变量等，可以导入模块去使用。

    常用的组合形式如下：
    import 模块名 【as 别名】
    from 模块名 import 类、变量、方法、模块、函数、* 【as 别名】
"""

# 使用import导入
import time     # time.py这个文件

time.sleep(2)   # 通过 . 就可以使用模块内部的全部功能（类、函数、变量）
print("等了2秒钟")

# 使用： from 模块名 import 功能名
from time import sleep      # 与import不同，目前只用time.py里面的sleep方法
sleep(1)
print("也可以")

# 别名
import time as t
t.sleep(1)
print("也行")

from time import sleep as sl
sl(2)
print("一样的")