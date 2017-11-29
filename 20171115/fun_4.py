# coding:utf-8
#***递归
#1.设定出口，递归的最底层
#2.递归一定要有return
#1.f(x)=f(x-1)+f(x-2)
#能用循环解决的事情不用递归
#请使用函数表达式表达f(x)
# def f(x,num):
#     print num
#     if x==1 or x==2:
#         return 1
#     else:
#         return f(x-1,num+1)+f(x-2,num+2)
#
# print f(10,0)

#2.阶乘
#5！=5*4*3*2*1
#输入一个数，显示他的阶乘结果

def g(x):
    if x==1:
        return 1
    else:
        return x*g(x-1)
print g(5)