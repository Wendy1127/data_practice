#coding:utf-8
#冒泡算法

list=[1,44,87,3,44,21,45]
for i in range(len(list)-1,0,-1):
    for j in range(0,i):
        if list[j]<list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
    # elif list[i]>=list[i+1]:

print list