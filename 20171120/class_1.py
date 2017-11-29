#coding:utf-8
#旧式类（经典类）
# class A():
#     pass
# #实例化
# a=A()
# print type(A)  #classobj 类
# print type(a)  #instance 实例化对象
# print a.__class__  #用于显示它的类型
# print A.__doc__  #显示类文档


#新式类（和继承有关）
# class B(object):
#     pass

class Person():
    #构造函数实现初始化操作
    #self   当前的类
    #Name='cctv'  #赋值，不建议这么使用
    def __init__(self,name,sex,age):
        #初始化类属性（变量）
        self.Name=name
        self.Sex=sex
        self.Age=age
        print self
    #真正意义上的构造函数
    def __new__(cls, *args, **kwargs):
        print cls
        print args
        print kwargs

fbb=Person('fbb','woman','30')
#调用类属性
print fbb.Age