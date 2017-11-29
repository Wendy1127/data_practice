#coding:utf-8
#匿名函数的一种形式
print [x for x in range(10) if x%2==0]

def a():
    list1=[]
    for x in range(10):
        if x %2==0:
            list1.append(x)
    return list1,1
def b(num):
    print [n**3 for n in num]
# b(a())

print a()
list1,num1=a()
print list1
print num1