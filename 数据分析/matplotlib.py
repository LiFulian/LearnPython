# coding=utf-8

from matplotlib import pyplot as plt

x = range(2, 24, 2)  # 数据在ｘ，ｙ轴的位置，是一个可迭代对象
y = [12, 23, 4, 23, 34, 24, 1, 12, 23, 34, 24]

# 设置图片大小（非必须）
plt.figure(figsize=(20, 10), dpi=80)

# 设置ｘ，ｙ轴刻度
# c = list(range(2, 20, 2))  # 步长为２
# print(c[::3])  切片操作，每三个取一个
# plt.xticks(x)

plt.plot(x, y)  # 绘图

# 设置ｘｙ轴刻度（非必须）
plt.xticks(range(4, 20, 2))
plt.yticks(range(min(y), max(y) + 3))

# 保存
# plt.savefig("./t1.png")

# 展示图片
plt.show()
