#coding:utf-8
#捕获异常
# try:
#     代码片段
# except<异常名>[,附加的数据]
#     异常处理

#1.可接受所有异常，使用BaseException
#2.else:假如上一层的except没有捕获到错误，所有的正常操作和异常就会掉到else中去处理
# try:
#     f=open('2.txt','w')
#     f.write('Hello World')
#
# except IOError:
#     print u'没有打开文件或者读取失败'
# # except BaseException,e:
# #     print e
# else:
#     print '111'

#3.finally 无论上面执行了什么，都会执行finally

# try:
#     f=open('2.txt','w')
#     f.write('Hello World')
#
# except RuntimeError:
#     print u'没有打开文件或者读取失败'
# except BaseException,e:
#     print e
# finally:
#     print 'finally'

#4.
try:
    try:
        f=open('2.txt','r')
        f.write('Hello World')
    finally:
        print 'finally'
except RuntimeError:
    print u'没有打开文件或者读取失败'
except BaseException,e:
    print e
