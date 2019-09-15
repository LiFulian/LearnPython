# 数据来源:https://www.kaggle.com/datasnaek/youtube/data
# 二维数组转置的方法 t.transpose()   t.T     t.swapaxes(1, 0)     最后一个是交换轴
# numpy中轴的概念,二维中,0->   1|   三维中 0/   1->  2|
import numpy as np

us_file_path = "./test1.csv"
uk_file_path = "./test2.csv"

t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int", unpack=True)
t2 = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

print(t1)
print("*"*100)
print(t2)

# 取行
print("*"*100)
print(t2[2])

# 取连续的多行
print("*"*100)
# print(t2[2:])
print(t2[2:5])

# 取不连续的多行
print("*"*100)
print(t2[[1, 3, 5]])

# 取
print("*"*100)
print(t2[1, :])
print(t2[2:, :])
print(t2[[1, 3, 5], :])
print(t2[:, 0])

# 取连续的多列
print(t2[:, 2:])

# 取不连续的多列
print(t2[:, [0, 3]])

# 取某行某列的值
a = t2[2, 3]
print(a)
print(type(a))

# 去多行和多列,如第3~5行,第2~4列
b = t2[2:5, 1:4]
print(b)

# 取多个不相邻的点,(0,1),(2,3)两个点
c = t2[[0, 2], [1, 3]]
print(c)

# 数值的修改
# 取过之后直接赋值

# 竖直拼接,vertically
np.vstack((t1, t2))

# 水平拼接(horizontally)
np.hstack((t1, t2))

# 行列交换
t1[[1, 2], :] = t1[[2, 1], :]  # 行交换




