#coding:utf-8
#数据封装
#1.实例方法
# class C:
#     def __init__(self):
#         pass
#     #设置属性值
#     def set_name(self,name):
#         self.Name=name
#
#     #获取属性值
#     def get_name(self):
#         return self.Name
#
# obj_c=C()
# obj_c.set_name('fzj')
# #实例化对象调用实例方法
# print obj_c.get_name()

# #2.静态方法,用到装饰器 尽量用新式类
# class Student(object):
#     count=0
#     books={}
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# 
#     # 装饰器
#     @staticmethod
#     def printClassAttr():
#         #操作的是类属性
#         #静态方法，属于类的一种方法，不属于实例化，只能操作类属性，并且没有参数限制及不需要实例参数和类参数
#         print Student.count
#         print Student.books
#
# stu=Student('name',10)
# #1.通过类名直接调用
# Student.printClassAttr()
# #2.通过实例化对象调用
# stu.printClassAttr()

#3.类方法
class School(object):
    #学生人数
    stu_num=0
    def __init__(self):
        pass
    #使用类方法装饰器
    @classmethod
    def printClass(cls):
        print cls.__name__
        print cls.__dict__

#只能通过类名调用类方法
School.printClass()
