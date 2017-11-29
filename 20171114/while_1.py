# coding:utf-8
#三要素
#1.起始值 2.终止值 3.步进值
#输入一个数值，输出从0到这个数的所有奇数。
# begin=0
# end=input(u'输入一个数：')
# step=1
# list1=[]
#
# if end%2==0:
#     end-=1
# while begin<=end:
#     if begin%2 ==1:
#         list1.append(begin)
#     begin+=step
# print list1

#range(begin,end,step)
end = input(u'输入一个数：')
for i in range(1,end,2):
    print str(i)+'\t'