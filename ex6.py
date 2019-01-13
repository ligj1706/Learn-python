#coding=utf-8
#定义变量
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)
#输出结果
print x
print y 
print "I said: %r." % x 
print "I also said:'%s'." % y 
#定义变量
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#输出结果
print joke_evaluation %	hilarious
#定义变量
w = "this is the left side of..."
e = "a string with a right side."
#输出结果
print w+e 
