#coding:utf-8
#访问控制
# public(公有)，protected(保护),private(私有)
# public,所有人都能用
# protected,只有子类能用
# private，只有自身类能用

#单下划线
#实现模块级别私有化（变量、函数、方法）
numA=10
_numA=100

def printNum():
    print 'numA is %d' % numA
    print 'numA is %d' % _numA

def _printNum():
    print 'numA is %d' % numA
    print 'numA is %d' % _numA

#双下划线