#coding:utf-8
import sys
#标准输出，默认输出到控制台
f =open('log.txt','w')   #以写模式
#保存标准输出的状态，默认状态为控制台
_console=sys.stdout
#修改标准输出的位置，
sys.stdout=f
print 1
print 2
print 3
#还原标准输出状态
sys.stdout=_console
print 1
print 2
print 3