from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

y_1 = [0, 0, 1, 0, 0, 1, 1, 2, 2, 1, 2, 2, 3, 2, 2, 1, 1, 1, 1, 1, 1]
y_2 = [1, 1, 1, 3, 3, 2, 4, 3, 2, 6, 4, 3, 4, 5, 4, 2, 3, 2, 2, 1, 1]
x = range(11, 32)

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# plt.plot(x, y_1)  # 绘图，

plt.plot(x, y_1, label="自己")  # 绘图，图例，字体在下面解决
plt.plot(x, y_2, label="同桌", color="cyan", linestyle=":", linewidth=10)
# 可以设置的属性，参考源码, 属性值错误时，控制台会显示可使用的值范围


# 设置ｘ轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_labels, fontproperties=my_font)
# plt.yticks(range(0, 7))

# 绘制网格
plt.grid(alpha=0.2)

# 添加图例，设置属性
plt.legend(prop=my_font, loc="upper left")  # 查看源码

# 展示
plt.show()