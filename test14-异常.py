"""
    异常 ： 程序运行的过程中出现了错误

    捕获异常 ： 提前假设某处出现异常，并且做好预处理，让程序继续执行下去
"""

# 基本的捕获语法
try:
    f = open("F:/python-object/bug.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("文件不存在")

# 捕获多个异常
try:
    1/0
    # print(myName)
except (NameError, ZeroDivisionError) as e:   # 通过 元组 的形式来写异常信息
    print(f"出现异常，异常内容是{e}")

# 捕获所有的异常  ----->>>>>>  常用
try:
    1/0
    # print(zzk)
except Exception as e:
    print("异常了")
else:                                     # 如果没有异常我会执行 else 中的雨具
    print("没有异常，一切正常")
finally:                                  # 无论有无异常，我都要执行
    print("我都要执行！！！")




# 异常的传递性
def func1():
    print("func1开始执行")
    num = 1/0
    print("func1结束执行")
def func2():
    print("func2开始执行")
    func1()
    print("func2结束执行")
def main():                               # 不需要去到func1函数里面去捕获，在高层这里也可以来捕获
    try:
        func2()
    except Exception as e:
        print("函数异常了")
main()
