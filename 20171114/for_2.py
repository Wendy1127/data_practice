#coding:utf-8
#引入math数学计算模块
from math import *  #可以直接使用sqrt
#import math         #要使用math.sqrt方式
#1.判断一个数是否是质数（素数）
#break,continue
#break 跳出（结束）循环
#continue跳过当前循环，进入下一循环
# for i in range(20):
#     if i==10:
#        continue
#     print i

# num =12
# s=0
# for i in range(2,13):
#     if num%i==0:
#         s =1
#         break
# if s ==1:
#     print  u'不是一个质数'
# else:
#     print u'是一个质数'

#2.取出0~100之间的所有质数
# for num in range(2,101):
#     #质数判断开始
#     s = 0
#     #循环遍历
#     for i in range(2, num):
#         if num % i == 0:
#             s = 1
#             break
#     #输出满足条件的质数
#     if s == 0:
#         print num
#

list2=[]
sum=0
for num in range(2,101):
    #质数判断开始
    s = 0
    #循环遍历
    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            s = 1
            break
    #输出满足条件的质数
    if s == 0:
        #print u'是一个质数',num
        sum +=num
print u'0-100中间所有质数和为：',sum

