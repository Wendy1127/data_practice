#coding:utf-8

# from class_5 import numA,_numA,printNum,_printNum
# from class_5_1 import *
# print numA
# print _numA
# printNum()
# _printNum()


#如果import后面用* 引入的时候会报错，下划线的变量或函数，不能被引入（模块级别的私有化）
from class_5 import *
print numA
printNum()

import *
# joke=Student('Joke',28)
# print joke.__address
print dir(class_5_2.joke)
