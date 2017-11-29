#coding:utf-8
#使用一个随机数模块，随机生成100个数，遍历数组，如果列表中出现10，则报异常

from random import *
list1=[]
for i in range(0,100):
    list1.append(randint(0,50))

if 10 in list1:
    #生成一个异常
    #raise,raise[exception name[,args]]
    try:
        raise Exception('having',5)
    except Exception:
        print 'having 10'
