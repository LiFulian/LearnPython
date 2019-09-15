from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

y_3 = [11, 14, 14, 16, 17, 15, 19, 14, 16, 19, 22, 18, 20, 24, 27, 26, 23, 27, 30, 32, 34,
       29, 35, 34, 29, 36, 34, 35, 34, 35, 34]
y_10 = [37, 36, 37, 34, 35, 30, 29, 30, 32, 29, 27, 25, 30, 32, 29, 27, 26, 29, 30, 26,
        25, 24, 22, 24, 20, 22, 16, 14, 13, 16, 10]

x_3 = range(1, 32)
x_10 = range(51, 82)

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 使用scatter方法绘制散点图，和之前的绘制折线图的唯一区别
plt.scatter(x_3, y_3, label="３月份")
plt.scatter(x_10, y_10, label="10月份")

#调整x轴的刻度
_x = list(x_3)+list(x_10)
_xtick_labels = ["3月{}日".format(i) for i in x_3]
_xtick_labels += ["10月{}日".format(i-50) for i in x_10]
plt.xticks(_x[::3], _xtick_labels[::3], fontproperties=my_font, rotation=45)

# 添加图例
plt.legend(loc="upper left", prop=my_font)

# 添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度", fontproperties=my_font)
plt.title("标题", fontproperties=my_font)

# 展示
plt.show()