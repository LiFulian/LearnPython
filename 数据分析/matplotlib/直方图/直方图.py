from matplotlib import pyplot as plt
from matplotlib import font_manager
# 使用原始数据，统计频数．
my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

a = [12,123,12,3,123,213,123,241,213,21,312,32,131,234,12,4,231,23,13,123,231,22,
     21,23,121,231,123,21,213,213,213,222,13,213,312,231,213,21,21,3,221,23,213,231,
    231,212,13,213,213,213,231,23,121,213,52,52,45,34,63,66,345,65,74,65,68,45,46]

plt.hist(a, 20)  # 自动分成20组

plt.show()
