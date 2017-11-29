# coding:utf-8
#二叉树
# def f(x):
#     if x==1 or x==2:
#         return 1
#     else:
#         return f(x-1)+f(x-2)

num=4
list=[1,1,1,1,2,3,3,2,1]
for i in range(num):
    for j in range(num-i):
        print ' ',
    list.append(list[i-1]+list[i-2])
    print list[i]