#导入模块
from sys import argv
#命令行参数
script, user_name = argv 
#raw_input函数
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to sak you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
comouter = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, comouter)