# _*_ coding:utf-8 _*_
# 使用Pygal 模拟掷骰子

from die import Die

# 创建一个D6实例
die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = [] # 用于储存每个点数出现的次数
for value in range(1, die.num_sides+1): # 遍历所有出现的点
    frequency = results.count(value) # 计算每种点数出现的次数
    frequencies.append(frequency) # 赋值到列表中

print(frequencies)