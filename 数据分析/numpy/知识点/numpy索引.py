# 布尔索引
import numpy as np
t = np.arange(24).reshape((4, 6))
print(t)

# print(t < 10)

# 布尔操作
# t[t < 10] = 0
# print(t)

# where操作
# print("*"*100)
# print(np.where(t < 10, 0, 10))

# clip三段裁剪
print(t.clip(10, 18))  # 小于10的替换为10, 大于18的替换成18