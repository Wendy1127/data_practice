#coding:utf-8
#open(file_name,mode)
#文件操作模式
#r 只读 r+读写（文件不存在则会报错）
#w 写 w+（文件不存在则会自动增加文件）
#a 追加 a+读写追加（在原文本的最后新增新的内容）

# #文件读取的操作
# filname=raw_input('enter file')  #输入文件名
# fobj=open(filname,'r')  #打开文件
# for eachline in fobj:  #遍历文件中的每一行
#     print eachline
# fobj.close()#关闭文件

#文件循环写入
f=open('4.txt','w')
for i in range(10):
    f.write(str(i))
f.close()