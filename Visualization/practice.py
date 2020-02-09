# _*_ coding: utf-8 _*_

# 类和实例
class Student(object):
    pass

bark = Student()
bark.name = "Bark simperson"
print(bark.name)

print(type(123))
type("123")
type("abc")

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = open('Users/Desktop/hello.py','r')