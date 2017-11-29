#coding:utf-8
# #read 读取文件所有内容
# f=open('3.txt')
# print f.read()


# #按行读取文本
# #（1）readline()读取一行文本
# f=open('3.txt','r')
# list1=[]
# #读取一行
# line=f.readline()
# #循环读取，直到读完
# while line:
#     #显示读取到的内容
#     print line.strip('\n')
#     #将内容放入列表中
#     list1.append(line.strip('\n'))
#     #再读下一行
#     line=f.readline()
# print list1
# #文件关闭
# f.close()

#(2)readlines()  按行读取，形成列表
f=open('3.txt','r')
list1=f.readlines()
print list1
f.close()