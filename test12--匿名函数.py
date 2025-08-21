"""
    1.函数作为参数传递
    2.lambda匿名函数
"""

# 1.函数作为参数传递
# 定义一个函数，接受另一个函数作为传入参数
def test_func(compute):
    result = compute(2,4)
    print(f"计算结果是: {result}")

def compute(x, y):
    return x + y
test_func(compute)


# 2.lambda匿名函数 -- 用来定义无名称的，它是一次性的，无法二次使用
# 关键字def 可以用来定义带有名称的函数
test_func(lambda x, y: x + y)