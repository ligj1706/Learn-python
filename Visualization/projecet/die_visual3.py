# _*_ coding:utf-8 _*_
# 绘制直方图

from die import Die
import pygal

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

# 对结果进行可视化
hist = pygal.Bar() #创造实例

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# 把值传递到直方图中
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

# print(frequencies)