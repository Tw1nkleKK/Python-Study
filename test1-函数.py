def add(x, y):
    result = x + y
    print(f"{x} + {y} = {result}")

add(2,4)


# 函数的说明文档
def deduce(x, y):
    """
    两数相减
    :param x: 形参
    :param y: 形参
    :return: 两数相减的结果
    """
    result = x - y
    print(f"{x} - {y} = {result}")
    return result

deduce(2,4)


# 函数嵌套
def func_b():
    print("---2---")

def func_a():
    print("---1---")
    func_b()
    print("---3---")

func_a()