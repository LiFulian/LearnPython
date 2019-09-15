# coding=utf-8
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# windows/linux 设置字体的方法
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}  # 参考rc源码
# # ctrl+b,查看源码demo
# # pass in the font dict as kwargs  # 两种写法
# matplotlib.rc('font', **font)

# 另一种设置字体的方式,下面需要传入my_font
my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")
# 传文件路径．查看fc-list :lang=zh

x = range(0, 120)
y = [random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)

# 调整ｘ轴刻度
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]

# 取步长，数字与字符串一一对应，数据的长度一样
# [::2]切片只能对列表操作，list(x)可以把可迭代对象x转换为数组
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45, fontproperties=my_font)

# 终端fc-list 查看linux/mac下面支持的字体，fc-list :lang=zh查看支持中文的字体
# x轴使用中文需要修改matplotlib的默认字体，matplotlib.rc可以修改，

# 添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度　单位(℃)", fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况", fontproperties=my_font)

plt.show()