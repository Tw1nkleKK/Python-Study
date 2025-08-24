""" 继承： 就是一个类，继承另一个类的成员变量和成员方法。
单继承语法：   class 类名(父类名): 类内容体
多继承语法：   class 类名(父1，父2，... ， 父N): 类内容体
"""
# 单继承
class Iphone:
    name = 'iphone11'
    producer = 'QBS'

    def call_by_4g(self):
        print("4g通话被调用")

class IphoneNew(Iphone):
    face_id = '10001'   #面部识别ID

    def call_by_5g(self):
        print("5G通话使用中...")

myPhone = IphoneNew()
print(myPhone.producer)
myPhone.call_by_4g()
myPhone.call_by_5g()

print("-----------------")
# 多继承
class NFCReader:
    nfc_type = "第五代"
    nfc_producer = "中兴"

    def read_card(self):
        print("NFC读卡中")
    def write_card(self):
        print("NFC写卡中")

class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")

class MyPhone(IphoneNew, NFCReader, RemoteControl):
    pass        # 不想添加任何东西了，补全语法用pass

zzkPhone = MyPhone()
zzkPhone.call_by_5g()
zzkPhone.write_card()
zzkPhone.control()

print(zzkPhone.producer)    # 输出同名的成员属性时，左边的优先，即谁先继承谁优先