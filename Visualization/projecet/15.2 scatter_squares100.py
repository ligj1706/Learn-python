# _*_ coding: utf-8 _*_
# 自动计算数据，绘制1000个点,颜色映射，文件保存

# 导入matplatlib中的pyplot模块并指定别名plt，原因避免反复输入pyplot
import matplotlib.pyplot as plt

# 创建包含x的列表，生成y值，遍历x中的值
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# 删除数据点轮廓edgecolor = 'none'，设置数据点颜色c='red'，还可以使用c=(o,o,1),分别表示红绿蓝
# plt.scatter(x_values, y_values, c='red', edgecolor = 'none', s=24)

# 删除数据点轮廓edgecolor = 'none'，颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
    edgecolor = 'none', s=24)

# 设置图表标题，给坐标轴加标签，设置文字大小
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 由于数值巨大，所以需设置每个坐标轴的取值范围，axis有四个数值，代表最小最大
plt.axis([0,5100, 0, 5001**3])

plt.show()

# 文件保存：plt.savefig('squares_plot.png', bbox_inches='tight')，第一个参数表示保存的文件名，第二个表示裁剪掉空白区域，可省略该参数