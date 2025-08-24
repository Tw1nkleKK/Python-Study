"""
    1.初识对象
"""
# 设计类
class Student:
    name = None
    gender = None
    age = None

# 创建对象
stu_1 = Student()

# 对对象赋值
stu_1.name = "zhouzikai"
stu_1.gender = "male"
stu_1.age = 18
print(stu_1)

"""
    2.类和成员方法、self关键字        类内部的函数称为方法，函数是类外部的。
# 类定义的属性（变量） --> 成员变量
# 类定义的行为（函数） --> 成员方法

# self 关键字，成员方法中必须要有self，但是传参的时候可以忽略它
"""
class StudentInfo:
    name = None

    def say_hi(self):
        print(f"大家好，我的名字是{self.name}，大家多多关照")
    def say_hi2(self, msg):
        print(f"大家好，我是{self.name},{msg}")       #想要访问成员属性必须使用self，外部传入的msg直接用就行

stu1 = StudentInfo()
stu1.name = "周杰伦"
stu1.say_hi2("哎哟，不错哦")