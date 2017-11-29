#coding:utf-8

#多重继承的一个顺序
class K1(object):
    def fo1(self):
        print 'K1-fo1'

class K2(object):
    def fo1(self):
        print 'K2-fo1'


class J1(K1,K2):
    def bar(self):
        print 'J1-bar'

class J2(K1,K2):
    pass

#子类
class C(J2,J1):
    pass

if __name__=='__main__':
    print C.__mro__          #继承关系调用顺序
    m=C()    #实例化
    m.fo1()
    m.bar()

#搜索方式，广度优先搜索
#fo1 调用顺序   C->J2->K1