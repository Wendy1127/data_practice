#coding:utf-8
#类属性和实例属性
# class A:
#     x=7  #类属性，静态数据
#     def __init__(self):
#         # self.x=a  #实例化属性
#         pass
#
# a=A()
# print A.x
# print a.x
# a.x=2
# a.y=A()
# print A.x
# print a.x
# print a.y.x  #类外拓展，实例（对象）属性


#练习,定义学生类
class Student:
    def __init__(self,sno,sname):
        # type: (object, object) -> object
        self.Sno=sno
        self.Sname=sname

stu1=Student(1,'f')
Student.school='bf'
stu1.school='beifeng'
stu2=Student(2,'z')
print dir(Student)
print dir(stu2)   #对象属性
print stu2.school
print Student.__name__

#特殊属性
#__doc__ 文档
#__init__ 初始化
#__module__ 类所属模块
#__name__  类名
#__dict__  等同于dir(object)，显示类的所有属性
