#coding:utf-8
import re  #python正则表达式模块
#生成一条正则表达式，匹配以h开头的字符串
# pattern=re.compile(r'^h*')
# pattern=re.compile(r'^h+')
# pattern=re.compile(r'^(h)+.*o$')
# #匹配，match执行正则表达式的匹配，从开头进行匹配，匹配不到返回Null
# result= re.match(pattern,'hello')
# if result:
#     #使用mathch对象取得分组信息
#     print result.group()
# else:
#     print 'Null'

#小练习
#验证输入的一串数字是否是手机号
pattern=re.compile('^1[3578]\d{9}$')
number=raw_input(u'请输入一个手机号')
#验证
if re.match(pattern,number):
    print u'这是一个手机号'
else:
    print u'请重新输入'