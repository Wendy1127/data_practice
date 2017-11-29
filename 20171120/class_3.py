#coding:utf-8
#self的作用,一个神奇的参数
class B:
    #self 接收实例化过程中传入的所有数据，这些数据是初始化函数后的参数导入的
    #self 就是一个具体的示例
    #self 主内
    def __init__(self):
        self.Name='ibf'
        print self
        print type(self)
    def get_name(self):
        print self.Name
    def show_name(self):
        self.get_name()
#a 主外
a=B()
#object.attribute  对象.属性
print a.Name
