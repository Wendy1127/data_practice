#coding:utf-8

class A:
    name='I am A'
    # def __call__(self, *args, **kwargs):
    #     return A.name
    # def __getattr__(self,item):
    #     self.item='1'
    #     return 'not have'+item
    #直接对象的时候显示内容，print 对象时被调用
    def __str__(self):
        return A.name


obj_a=A()
print dir(obj_a)
