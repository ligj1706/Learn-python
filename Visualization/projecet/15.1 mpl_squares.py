# _*_ coding: utf-8 _*_

# 导入matplatlib中的pyplot模块并指定别名plt，原因避免反复输入pyplot
import matplotlib.pyplot as plt

# 给plot同时提供输入值和输出值，增加输入值
input_values = [1, 2, 3, 4, 5]
# 创建列表
squares = [1, 4, 9, 16, 25]
# 线条宽度
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题，给坐标轴加标签，设置文字大小
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)

# 打开matplotlib查看器，并绘制图形
plt.show()



