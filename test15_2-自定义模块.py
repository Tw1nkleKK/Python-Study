"""
    自定义的在 “tools” 中
"""

# 导入自定义方法1
import tools.my_module1
tools.my_module1.test(1,2)

# 导入自定义方法2
from tools.my_module1 import test
test(2,3)


# __main__ 变量
# 在模块中运行时，会把内置变量 __name__ 设为 __main__。所以在模块中运行时会执行下面的测试代码
# 但导入这个模块时，不会执行测试代码


# __all__ 变量
# 如果一个模块文件中有'__all__'变量，当使用 ‘ from XXX import * ’ 来导入时，只能导入这个列表中的元素
# * 代表所有，来自 all 变量的定义
# * 能限制导入，但不用*的话正常导入一样能导入，只是限制
from tools.my_module1 import *
test_a()
#test_b() 被all变量限制