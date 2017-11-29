#coding:utf-8
#双下划线,一定程度私有化
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__address='上海'

joke=Student('Joke',28)
# print joke.__address
print joke._Student__address
#类内的双下划线的内容，类外调用使用，被改为属性前面加上单下划线和类名 _类名__属性