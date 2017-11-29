#coding:utf-8

#人类（父类）
class Person:
    #说话
    def speak(selfs):
        print '妈妈'
    #设置身高
    def setHeight(self,h):
        self.Height=h
    #跑步
    def run(self):
        print 'I can running'

class Man(Person):
    def have_hj(self):
        print 'I have 喉结'

class Boy(Man):
    #重写父类方法，重载
    def setHeight(self):
        print 'The height is 1.7m'

# #女孩（子类）
# class Girl(Person):
#     def setHeight(self):
#         print 'The heigth is 1.7m'

#主函数，入口文件
#默认执行的内容
if __name__=='__main__':
    cang=Boy()
    # cang=Girl()
    cang.setHeight()  #重写了父类
    cang.speak()  #父类
    cang.run()  #父类
    cang.have_hj()
