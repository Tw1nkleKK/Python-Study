# 局部变量: 作用在函数内部，在函数外部无法使用
def test_a():
    num = 100
    print(num)

test_a()
# print(num)

print("-----------------------------------")

# 全局变量: 在函数内部和外部均可使用
# global关键字，可以在函数内部声明变量为全局变量
number = 200

def test_b():
    print(number)

def test_c():
    global number
    number = 300
    print(number)

test_b()
test_c()
print(number)