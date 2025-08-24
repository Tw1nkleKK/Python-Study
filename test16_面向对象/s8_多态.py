"""
    多态：多种状态。
    同样的行为(函数)，传入不同的对象，得到不同的状态。
"""

# 初识多态
class Animal:
    def speak(self):              # 空实现：优点是父类用来确定有哪些方法。具体的实现由子类完成。
        pass                      # 这种写法，就叫抽象类（也可以叫做 接口） ； 这里speak方法 就叫 抽象方法。

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)

# 抽象类（接口）：定义一个标准，它包含一些抽象方法，要求子类必须实现。
# 举例：空调
class AC:
    def cool_wind(self): pass        # 制冷
    def hot_wind(self): pass         # 制热
    def swing_left_right(self): pass #左右摆风

class Midea_AC(AC):
    def cool_wind(self): print("美的制冷")
    def hot_wind(self): print("美的制热")
    def swing_left_right(self): print("美的左右摆风")

class Green_AC(AC):
    def cool_wind(self): print("格力制冷")
    def hot_wind(self): print("格力制热")
    def swing_left_right(self): print("格力左右摆风")

def make_cool(ac: AC):
    ac.cool_wind()

midea_ac = Midea_AC()
green_ac = Green_AC()

make_cool(midea_ac)
make_cool(green_ac)