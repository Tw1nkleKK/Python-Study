# 列表的遍历 --> while & for

def list_while_func():
    my_list = ['zzk', 111, 666, True]
    index = 0
    while index < len(my_list):
        print(my_list[index])
        index += 1

def list_for_func():
    my_list = ['zzk', 111, 666, True]
    for item in my_list:
        print(item)

list_while_func()
print("----------")
list_for_func()