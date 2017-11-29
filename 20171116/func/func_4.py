#coding:utf-8
#装饰器
# def foo():
#     print 'i am foo'
#在方法被调用输出foo is running，结束时，输出foo end
# def show(func):
#     def wrapper(*args,**kwargs):
#         print '%s is running'%(func.__name__)
#         func(*args,**kwargs)
#         print '%s end'%(func.__name__)
#     return wrapper
#
# def foo1():
#     print 'i am foo1'
#
# foo1=show(foo1)
# foo1()

#练习
#装饰器语法糖
#执行打印时间差，并计算a+b总和操作
# import time
# def deco(func):
#     def wrapper(a,b):
#         startTime=time.time() #返回秒
#         func(a,b)  #睡眠，执行综合计算
#         endTime=time.time()
#         msecs=(endTime-startTime)*1000 #差值毫秒形式显示
#         print u'时间差为：%f ms'% msecs
#     return wrapper
# def deco(func):
#     def wrapper(*args,**kwargs):
#         print 'deco'
#         func(*args, **kwargs)
#         print 'deco end'
#     return wrapper
# def deco2(func):
#     def wrapper(*args,**kwargs):
#         print 'deco2'
#         func(*args, **kwargs)
#         print 'deco2 end'
#     return wrapper
#
#
# # deco(deco2(addFunc(a,b)))
# @deco
# @deco2
#
# def addFunc(a,b):
#     print 'start addFunc'
#     print 'Result:%d'%(a+b)
#     print 'end addFunc'
# addFunc(3,8)

#练习2
#传入一个列表，判断长度，生成状态值
#如果列表长度小于5，则状态值为1，否则为2
#使用状态值传入一个函数内，函数内判断状态值，执行不同的操作
def len_list(func):
    def warpper(*args,**kwargs):
        #数据过滤的一个过程
        if len(*args)<5:
            func(1,1,*args)
        else:
            func(2,2,*args)
    return warpper
@len_list
def go_list(num,num2,list):  #没有传num值，通过装饰器传入了num
    print num,num2,list

go_list(range(3))