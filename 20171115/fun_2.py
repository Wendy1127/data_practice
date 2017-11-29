#coding:utf-8
def fun(a):
    return a**2

#传入两个参数，第一个参数表示函数名，第二个参数表示值
def get_fun(f,num):
    return f(f(num)+1)

print get_fun(fun,2)

