"""
    字符串是字符的容器，一个字符串可以存放任意数量的字符。

    同 元组 一样，它是不可修改的数据容器。
"""

# 1.通过下标索引来取值
name = "周子凯"
value1 = name[0]
value2 = name[-3]
print(value1, value2)

# 2.index方法
num = name.index("凯")
print(num)

# 3.replace方法：将字符串内的 字符串1 替换为 字符串2。不是修改字符串本身，而是得到一个新字符串
my_str = "zhou and zi and kai"
my_str1 = my_str.replace("and", "&")
print(my_str)
print(my_str1)

# 4. 字符串分割的方法：split。 按照指定的分隔符将字符串划分为多个字符串，并存入列表对象中。 字符串本身不变，得到一个列表对象。
zzk_str = "zhou zi kai"
zzk_str_list = zzk_str.split(" ")
print(f"切分的结果是{zzk_str_list},类型是{type(zzk_str_list)}")


# 5. 字符串的规整操作（去前后空格）：strip()   ----无参数
my_str = " zhou zi kai "
print(my_str)
print(my_str.strip())

# 6.字符串的规整操作（去前后指定字符串）：strip(字符串)   ----有参数
my_str = "12zhou zi kai 221"
print(my_str.strip("12"))


# 7.count方法
my_str = "12zhou zi kai zi221"
count = my_str.count("zi")
print(count)

# 8。len()方法
my_str = "12zhou zi kai 221"
print(len(my_str))


# 9. 字符串遍历 while 和 for 。    同列表和元组的遍历一样。

"""
    字符串：
        1.只可以存储字符串
        2.长度任意
        3，支持下标索引
        4，允许重复字符串出现
        5，不可以修改
        6.支持for循环
"""