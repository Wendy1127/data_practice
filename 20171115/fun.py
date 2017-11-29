#coding:utf-8
#自定义一个函数
#封装质数判断
#return 结束函数，返回一个值或者多个值给调用方
import math
def _zhishu(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return 1
    return 0
#函数调用
a=_zhishu(13)
print a

def returnMore():
    '''
    返回多个值
    :return: 1，2，3，4，5
    '''
    return 1,2,3,4,5

print returnMore.__doc__
q=0
x=returnMore()
for val in x:
    print val

#x=1,y=2请用三行语句交换他
#1.可以使用中间变量，暂时存储某个值
x=1
y=2
temp=x
x=y
y=temp

print x,y

#2.不使用中间值，直接交换
x=1
y=2
x=x+y
y=x-y
x=x-y

print x,y

#3.
x=1
y=2
y,x=x,y
print x,y

#函数的结构
def functionname(arg):
    # '函数文档描述字符串'
    # 函数主体部分
    # return (返回值)