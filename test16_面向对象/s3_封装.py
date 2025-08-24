"""
    封装：将现实世界事物在类中描述为属性和方法。

    私有成员：现实世界中有部分属性和行为是不公开对使用者开发的，在类中也是这样，就定义了私有成员
    如何定义私有成员？ 成员变量和方法的命名以__作为开头
    私有成员的访问限制： 类对象无法访问私有成员； 类中其他成员可以访问私有成员。
"""
class Phone:
    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

iphone = Phone()
iphone.call_by_5g()