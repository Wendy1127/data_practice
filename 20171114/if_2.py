#coding:utf-8
#判断奇偶性，使用raw_input作为入口
#eval()自动转换数据类型
num = eval(raw_input(u'请输入一个数字：'))
if num%2 == 1:
    print  u'你输入了一个奇数'
else:
    print  u'你输入了一个偶数'