# coding:utf-8
#请写出一段代码实现删除一个list里面的重复元素
# list1=[1,2,3,4,5,4,3,2,1]
# # print set(list1)
# #定义一个新的列表
# list2=[]
# #遍历列表
# for i in list1:
#     #判断list2是否存在当前值
#     if i not in list2:
#         list2.append(i)
# print list2

#已知列表[123，123，13，546，312，63，124，61，37，1278，19320，10]，请使用冒泡排序进行倒叙排序列表
#冒泡排序
# list2=[123,123,13,546,312,63,124,61,37,1278,19320,10]
# list2_len=len(list2)
# #使用i控制排序次数
# for i in range(0,list2_len-1):
#     #使用j控制比较次数，并且使用j来控制，当前要比较的下标
#     for j in range(0,list2_len-1-i):
#         #判断当前项是否小于后一项，如果满足条件，则进行交换
#         if list2[j]<list2[j+1]:
#             list2[j],list2[j+1]=list2[j+1],list2[j]
#
# print list2

#选择排序
list2=[123,123,13,546,312,63,124,61,37,1278,19320,10]
list_len=len(list2)
for i in range(list_len):
    #遍历剩余列表，找到列表中最小值的下标
    min_index=0
    #遍历确定当前范围的最小值的下标
    for j in range(list_len-i):
        #比较最小值的下标对应的值和当前项的值
        if list2[min_index]>list2[j]:
            #当前项小的话，min_index重新赋值
            min_index=j
    list2[list_len-i-1],list2[min_index]=list2[min_index],list2[list_len-i-1]
print list2