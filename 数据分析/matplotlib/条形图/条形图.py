from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

a = ["速度与激情", "战狼２", "功夫瑜伽", "西游降魔", "最后的骑士"]

b = [24, 17, 47, 34, 20]

# 设置图形的大小
plt.figure(figsize=(20, 15), dpi=80)

# 绘制条形图
# plt.bar(range(len(a)), b, width=0.3)　# 竖条形图
plt.barh(range(len(a)), b, height=0.3)  # 横条形图

# 设置字符串到x轴
plt.yticks(range(len(a)), a, fontproperties=my_font)

# 添加网格
plt.grid(alpha=0.3)

# plt.savefig("./movie.png")

plt.show()