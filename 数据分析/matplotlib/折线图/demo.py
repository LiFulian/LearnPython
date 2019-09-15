from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")


y = [1, 0, 1, 3, 3, 2, 4, 3, 2, 6, 4, 3, 4, 5, 4, 2, 3, 2, 2, 1, 1]
x = range(11, 32)

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)

# 设置ｘ轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_labels, fontproperties=my_font)
plt.yticks(range(0, 9))

# 绘制网格
plt.grid(alpha=0.2)

# 展示
plt.show()