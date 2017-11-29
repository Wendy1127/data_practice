#coding:utf-8
#实现九九乘法表
#1.实现直角三角形的打印，输入一个数值，输出m行m列的三角形
# *
# **
# ***
# ****
# .....

#（1）获取输入的值
num =input(u'请输入三角形的行数：')
#i表示行数
for i in range(num):
    #j代表行数
    for j in range(i+1):
        print '*',
    print

#i表示行数
for i in range(num):
        print '*'*(i+1)
#（2）外层for 里面两个并列for,center(),两次字符串重复
#外层for里面两个并列for
num =input(u'请输入三角形的行数：')
#i表示行数
# list =[]
# for m in range(num):
#     list.append(m)
for i in range(num,1,-1):
    #j来控制打印倒三角，倒三角有空格组成，当前空格数量为总行数-当前行数-1
    for j in range(num-i):
        print '',
    #k 来控制打印“*”，当前输出的数量为行数（i+）
    for k in range(i-1):
        print '*',
    print


#2.center()
#      *
#     **
#    ***
#   ****
# .....
#
num =input(u'请输入三角形的行数：')
#i表示行数
for i in range(num):
    str=''
    for i in range(i+1):
        str+='* '
    print str.center(2*num)

#3.两次字符串重复j
num =input(u'请输入三角形的行数：')
for i in range(num):
    print ' '*(num-i)+'* '*(i+1)

# #4.center +-一次字符串重复

num =input(u'请输入三角形的行数：')
for i in range(num):
    s = ' '
    print str('* '*(i+1)).center(2*num)

#5.九九乘法表
# 1*1=1
# 2*1=2 2*2=4
# ......
# i 控制行数，即乘数
for i in range(1,10):
    for j in range(1,i+1):
        print  '%d*%d=%2d'%(i,j,i*j),
    print
