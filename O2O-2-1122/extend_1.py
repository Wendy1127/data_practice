def a():
    for i in range(10):
        yield i
def b():
    for i in range(10):
        return i

for item in a():
    print item
print b()