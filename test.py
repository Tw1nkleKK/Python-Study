print("hello world")

def add(a,b):
    return a+b

x = add(1,2)
print(x)

print("======================================")
"""
    写一个函数统计字符串的长度
"""
str1 = "i am boy"

count = 0
for i in str1:
    count += 1
print(count)

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")

my_len(str1)