"""
    数据容器： 一种可以存储多个元素的Python数据类型。
    数据容器分为 5 大类：
        列表list，元组tuple，字符串str，集合set，字典dict

    是否支持重复元素
    是否可以修改
    是否有序
"""


"""
    1.列表: 可存储不同的数据类型，支持嵌套
    变量名称 = []
    变量名称 = list()
    
    列表可以容纳多个元素；
    可以容纳不同类型的元素（混装）；
    数据是有序存储的（有下标序号）；
    允许重复数据存在；
    可以修改（增加或删除元素等）。
"""
my_list = ['zzk', 111, 666, True]
my_list1 = [[1,2,3], [4,5,6]]   # 嵌套列表
print(my_list)
print(type(my_list))
print(my_list1)
print(type(my_list1))

# 下标索引
zzk_list = ['z', 'z', 'k', 1, 9, 9, 7]
print(zzk_list)

print(zzk_list[-1])

# 嵌套列表
zzk_list1 = [[1,2,3], [4,5,6]]
print(zzk_list1[1][2])

# 列表常用操作--插入、删除、清空、修改、统计元素个数
# 函数def 定义为class类的成员，那么函数称之为 方法
class Student:
    def add1(self, x, y):
        return x + y

student = Student()
numbers1 = student.add1(1,2)
print(numbers1)

print("==============================")

list1 = ["zzk", "zhou", "zi", "kai"]
# 列表方法1-->查找某元素的下标  语法：列表.index(元素)
index = list1.index("zzk")
print(index)

# 列表方法2-->修改
list1[-4] = "zhouzikai"
print(list1)

# 列表方法3-->插入 insert
list1.insert(1, "name")
print(list1)

# 列表方法4-->追加 append 到列表尾部
#        -->追加一批元素 extend
list1.append("zzk")
print(list1)
list2 = [8, 8, 8, "wo"]
list1.extend(list2)
print(list1)

# 列表方法5-->删除指定下标索引的元素(2种方式)
# del 列表名[下标]
# 列表.pop(下标)
z_list = ["zzk", "zhou", "zi", "kai"]
del z_list[0]
print(z_list)
element = z_list.pop(0)
print(f"删除的元素是{element}，删除后的元素是{z_list}")
# 删除某元素在列表中的第一个匹配项
# 列表名.remove(元素)
zk_list = ["z", "z", "k", 1, 9, 9, 7]
zk_list.remove("z")
zk_list.remove(9)
print(zk_list)

# 列表方法6-->清空列表
zk_list.clear()
print(f"列表被清空了，结果是{zk_list}")

# 列表方法7-->统计某元素在列表种的数量
# 列表名.count(元素)
kk_list = ["z", "z", "k", 1, 9, 9, 7]
print(kk_list.count("z"))

# 列表方法8-->统计列表有多少元素
# len(元素)
kkK_list = ["z", "z", "k", 1, 9, 9, 7]
count = len(kkK_list)
print(f"列表中元素的个数有{count}个")

"""
    列表.append(元素)       ：向列表中追加一个元素
    列表.extend(容器)       ：将 数据容器 的内容依次取出，追加到列表尾部
    列表.insert(下标，元素)  ：在指定下标处，插入指定的元素
    del 列表[下标]          ：删除
    列表.pop(下标)          ：删除
    列表.remove(元素)       ：从前到后，删除第一个匹配项
    列表.clear()           ：清空列表
    列表.count(元素)        ：统计元素在列表中出现的次数
    列表.index(元素)        ：查找指定元素在列表的下标
    len(列表)              ：统计容器内有多少个元素
"""