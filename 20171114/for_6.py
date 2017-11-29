#coding:utf-8
#实现菱形

num =input(u'请输入三角形的行数：')
#i表示行数
list1=[]
for i in range(num):
    for j in range(num-i):
        print ' ',
    list1.append('*')
    print list1[0],
    for k in range(i*2):
        print ' ',
    print list1[i]
for m in range(num,0,-1):
    for n in range(num-m):
        print ' ',
    list1.append('*')
    print ' ',list1[0],
    for p in range((m-1)*2):
        print ' ',
    print list1[m]