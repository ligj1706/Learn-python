# _*_ coding:utf-8 _*_
# 同时投两个面数不相同的骰子

from die import Die

import pygal

# 创建两个D6实例
die_1 = Die()
die_2 = Die(10)

# 将结果储存在一个列表
results = []
for roll_num in range(500000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = [] # 用于储存每个点数出现的次数
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1): # 计算各种点出现的次数
    frequency = results.count(value) # 计算每种点数出现的次数
    frequencies.append(frequency) # 赋值到列表中

# 对结果进行可视化
hist = pygal.Bar() #创造实例

#标题、横纵坐标及刻度
hist.title = "Results of rolling a D6 and a D10 50,000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9',
                '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# 把值传递到直方图中
hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')

# print(frequencies)