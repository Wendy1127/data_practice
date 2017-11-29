# coding:utf-8

# 继承之调用父类构造方法
# super 调用父类方法
__metaclass = type  # 设定特定函数


class A(object):
    def __init__(self):
        self.b = 90
    def show_b(self, name):
        print '%s is about %s' % (name, self.b)

class C(A):
    def __init__(self):
        # 调用父类初始化方法
        # super(子类的类名,实例化对象).父类方法
        super(C, self).__init__()
        self.d = 80
    def show_b(self, name):
        super(C, self).show_b('aaa')
        print '%s is about %s,%s' % (name, self.b, self.d)

c = C()
c.show_b('a')
