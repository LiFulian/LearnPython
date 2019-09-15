# 更多应用
# １．用户的年龄分布
# ２．一段时间内用户点击次数的分布状态
# ３．用户活跃时间的分布


# 使用条形图解决的
from matplotlib import pyplot as plt
from matplotlib import font_manager

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
# width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3745, 4535, 3422, 2344, 3452, 1234, 234, 132, 31, 24]

# print(len(interval), len(width), len(quantity))

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

plt.bar(range(12), quantity, width=1)

# 设置ｘ轴的刻度
_x = [i-0.5 for i in range(13)]

_xtick_labels = interval+[150]

plt.xticks(_x, _xtick_labels)

plt.grid()
plt.show()