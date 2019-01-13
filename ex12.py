#coding=utf-8
#定义时必须放在括号中才能够运行
age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weight?")
#输出内容中没有具体的数字，关键原因还未找到
print "So, you're %r old, %r tall and %r heavy." % (
   age, height, weight)