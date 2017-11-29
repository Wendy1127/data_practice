#coding:utf-8
from random import *
#生成一个[a，b]随机整数
print randint(1,3)
#生成一个[a,b)随机整数
print randrange(1,3)
#打乱一个序列
list1=[1,2,3,4,5,6,7]
print shuffle(list1)
print list1

#生成一个[0.0,1)随机浮点数
#等同于randrange
a=1
b=2
print int(random()*(b-a))+a
#生成一个[a,b]之间的浮点数
print uniform(1,2)

import math
print math.pi