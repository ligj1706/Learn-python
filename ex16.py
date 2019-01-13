#coding=utf-8
#定义参数
from sys import argv
#把文件名定义为参数
script, filename = argv
#为计算机解释需要打开的文件
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
#在文件中键入每行的内容
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#直接为以下输出结果
print "I'm going to write there to the file."
#命令键入内容
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#直接输出以下内容
print "And finally, we close it."
target.close()
