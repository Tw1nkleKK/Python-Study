"""
    复写：子类在继承父类的成员属性和成员方法后，如果不满意，则可以进行复写。
    即：在子类中重新定义同名的属性和方法即可。
"""

class Watch:
    sid = None
    producer = "小米"

    def func(self):
        print("看时间")

class MyWatch(Watch):
    producer = "zzk"

    def func(self):
        print("通话、wechat、看时间、闹钟...")

        # 方法一
        print(f"父类的厂商是{Watch.producer}")
        Watch.func(self)
        #方法二
        print(f"父类的厂商是{super().producer}")
        super().func()

zzkWatch = MyWatch()
print(zzkWatch.producer)
zzkWatch.func()


# 调用父类同名成员名，一旦复写则调用的是复写后的新成员
# 若需要使用被复写的父类的成员，需要特殊的调用方式
"""  子类调用父类的成员
方法一：调用父类成员
父类名.成员变量
父类名.成员方法(self)

方法二：使用 super() 调用父类成员
super().成员变量
super().成员方法()
"""
