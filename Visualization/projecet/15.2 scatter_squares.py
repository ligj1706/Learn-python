# _*_ coding: utf-8 _*_
# 使用scatter()绘制散点图并设置其样式

import matplotlib.pyplot as plt

# 设置单个点scatter 为函数,s=20 为点的尺寸,（2，4）为绝对坐标
# plt.scatter(2, 4, s=20)

# 设置多个点
x_values = [1, 2, 3, 4,5]
y_values = [1, 4, 9,16,25]
plt.scatter(x_values, y_values, s=100)

# 设置图表标题，给坐标轴加标签，设置文字大小
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小，which='major'为主刻度
plt.tick_params(axis='both', which='major',labelsize=14)

plt.show()