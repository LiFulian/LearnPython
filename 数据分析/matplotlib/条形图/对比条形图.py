from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

a = ["速度与激情", "战狼２", "功夫瑜伽", "西游降魔", "最后的骑士"]

b_14 = [24, 17, 47, 34, 20]
b_15 = [37, 18, 23, 45, 32]
b_16 = [12, 23, 43, 12, 43]

bar_width = 0.2

x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width*2 for i in x_14]

# 设置图形的大小
plt.figure(figsize=(20, 15), dpi=80)

# 绘制条形图
plt.bar(range(len(a)), b_14, width=bar_width, label="9月14")  # 竖条形图
plt.bar(x_15, b_15, width=bar_width, label="9月15日")
plt.bar(x_16, b_16, width=bar_width, label="9月16日")

# 设置图例
plt.legend(prop=my_font)

# 设置字符串到x轴
plt.xticks(x_15, a, fontproperties=my_font)

# 添加网格
plt.grid(alpha=0.3)

# plt.savefig("./movie.png")

plt.show()