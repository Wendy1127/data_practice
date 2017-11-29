#coding:utf-8
#不定长参数
def printInfo(arg1,*vartuple):
    print u'输出'
    print arg1
    for var in vartuple:
        print ','+str(var)

printInfo(10)
printInfo(70,60,50)