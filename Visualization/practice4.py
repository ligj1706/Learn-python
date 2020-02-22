# _*_ coding:utf-8 _*_
# 通过requests 下载指定网页文件并储存

# 输入模块
import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

# 检验是否可进行下载
res.raise_for_status()

# 以写二进制的方式打开文件
playFile = open('RomeoAndJuliet.txt', 'wb')

# 通过循环遍历文件
for chunk in res.iter_content(1000000):
    playFile.write(chunk)

# 关闭文件
playFile.close()