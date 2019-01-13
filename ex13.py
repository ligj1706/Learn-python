#coding=utf-8
#参数个数必须充足，如果个数不足则会发生相应错误
from sys import argv

script, first, second, third = argv
#可随意换参数，参数的值可以随意赋予，不同的赋予结果将会得到不同的答案
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
