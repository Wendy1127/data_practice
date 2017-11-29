#coding:utf-8
#(1) @ 前后都有任意长度单词或数字
#(2) 一定存在.com或.cn等类型，（.加上2-3位字母） 出现次数1-2
import re
pattern=r'\w+@\w+(\.\w{2,3}){1,2}'
string=raw_input(u'请输入一个邮箱地址：')
if re.match(pattern,string):
    print 'yes'
else:
    print 'no'


#字符串数据提取
string='<span>地点：上海-长宁区</span><span>公司性质：外商独资</span>'
#(1)split切割
# pattern=re.compile(r':')
# result=re.split(pattern,string)
# print result[1]

#(2)数据正则提取,
# 贪婪模式
# pattern=re.compile(r'<span>地点：(.*)</span>')
# print re.findall(pattern,string)
# 非贪婪模式
pattern=re.compile(r'<span>(.*?)：(.*?)</span>')
print re.findall(pattern,string)
for item in re.findall(pattern,string):
    for i in item:
        print i
