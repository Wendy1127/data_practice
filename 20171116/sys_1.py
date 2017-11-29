#coding:utf-8
# from func.func_2 import a
# print a()
#sys.stdin标准输入
import sys
while True:
    print '请输入一个列表，以空格分割：',
    line=sys.stdin.readline()   #等同于raw_input()
    if not line:  #判断输入的是否为空行,line是空行，not line即为真
        break     #推出程序不继续输入
    else:
        a=line.split('')
    print a