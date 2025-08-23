"""
    从物理上看，包就是一个文件夹，文件夹下包含 __init__.py , 该文件夹可用于包含多个模块文件
    从逻辑上看，包的本质是模块

    包的作用：当我们写的模块越来越多时，可以帮助我们来管理所有的模块
    有 __init__.py 它就是包，没有的话就是一个普通的文件夹
"""

# 三种导包形式
import tools.my_module1
tools.my_module1.test_a()

from tools.my_module2 import test
test(20, 10)

from tools import my_module2
my_module2.test(30, 10)

# 通过 __all__ 变量， 控制 import *
# 看 tools 中的 __init__.py 文件。




# 安装第三方包 ： pip install 包名
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy