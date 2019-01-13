#coding=utf-8
#犯过的错误：单词输入错误，大小写书写错误，中英文标点出错
#定义变量内容
formatter = "%r %r %r %r"
#打印数字
print formatter % (1, 2, 3, 4)
#打印单词
print formatter % ("one", "two", "three", "four")
#打印单词，不用加引号
print formatter % (True, False, False, True)
#打印有定义的变量
print formatter % (formatter, formatter, formatter, formatter)
#打印句子
print formatter % (
      "I had this thing.",
	  "That you didn't sing.",
	  "But it didn't sing.",
	  "So I said goodnight."
	  )