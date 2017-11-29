#coding:utf-8
#已知第一个数为1，第二个数为1，并且满足等式f(x)=f(x-1)+f(x-2),请计算f(100)的值（斐波那契数列）

list1=[]
list1.extend([1,1])
#已知得到2个数值，所以下标从2开始
for i in range(2,100):
    #计算当前列表值
    list1.append(list1[i-2]+list1[i-1])
    print list1[i]
print  u'f(100)为',list1[99]


