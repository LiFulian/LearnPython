from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

# 使用原始数据，统计频数．
a = [12,123,12,3,123,213,123,241,213,21,312,32,131,234,12,4,231,23,13,123,231,22,
     21,23,121,231,123,21,213,213,213,222,13,213,312,231,213,21,21,3,221,23,213,231,
    231,212,13,213,213,213,231,23,121,213,52,52,45,34,63,66,345,65,74,65,68,45,46]

# 计算组数
d = 20  # 分组的步长,
num_bins = (max(a)-min(a))//d  # 不整除的时候，可能错位
print(max(a), min(a),max(a)-min(a))
print(num_bins)

# 设置图形的大小
plt.figure(figsize=(20, 8), dpi=80)

# plt.hist(a, num_bins)  # 频数分布
plt.hist(a, num_bins, n)

# 设置x轴的刻度
plt.xticks(range(min(a), min(a)+num_bins*(d+1), d))

plt.grid()

plt.show()
