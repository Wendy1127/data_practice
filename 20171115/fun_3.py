# coding:utf-8
# 不可更改参数
b = 2
def get_num(a):
    a = 10

get_num(b)
print b

# 可更改参数
list1 = [1, 2, 3]
def set_list(list2):
    list2.append([1, 2])

set_list(list1)
print list1
