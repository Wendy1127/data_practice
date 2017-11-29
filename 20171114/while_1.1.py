# coding:utf-8
#三要素
#1.起始值 2.终止值 3.步进值
#输入一个数值，输出从1到这个数的所有奇数。
begin=1
end=input(u'输入一个数：')
step=2
list1=[]

if end%2==0:
    end-=1
while begin<=end:
    if begin%2 ==1:
        list1.append(begin)
    begin+=step
print list1