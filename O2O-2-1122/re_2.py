#coding:utf-8
import re
#（1）
# string='hello world hello world'
# pattern=re.compile(r'(\w+)+')
# #匹配整个字符串，类似于match
# result=re.search(pattern,string)
# print result
# if result:
#     print result.groups()
#
#
# (2)split，以匹配到的内容进行字符串的切割
# string='hello world world'
# pattern=re.compile(r'l')
# result=re.split(pattern,string)
# print result

#(3)findall 搜索整个字符串，得到所有匹配的结果
# string='one1two2three3four4'
# patten=re.compile('(\d+)')
# print re.search(patten,string).group()
# print re.findall(patten,string)

#(4)finditer() 返回一个顺序访问每个匹配结结果的match对象的迭代器
# string='one1two2three3four4'
# patten=re.compile('(\d+)')
# for item in re.finditer(patten,string):
#     print item.group()

#(5)sub()  使用replace模式 替换string中每一个被匹配到的字符串，返回替换完的字符串
string='i say,hello world'
patten=re.compile('(\w+) (\w+)')
print re.sub(patten,r'\2 \1',string)