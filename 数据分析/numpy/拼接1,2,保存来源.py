import numpy as np

t1_data = "./test1.csv"
t2_data = "./test2.csv"

# 加载数据
t1_data = np.loadtxt(t1_data, delimiter=",", dtype=int)
t2_data = np.loadtxt(t2_data, delimiter=",", dtype=int)

# 添加来源
# 构造数据
zeros_data = np.zeros((t1_data.shape[0], 1)).astype(int)
ones_data = np.ones((t2_data.shape[0], 1)).astype(int)

# 分别添加一列全为0,1的数组
t1_data = np.hstack((t1_data, zeros_data))
t2_data = np.hstack((t2_data, ones_data))

# 拼接两组数据
final_data = np.vstack((t1_data, t2_data))
print(final_data)

# node
# 1.获取最大值最小值的位置
#     1.np.argmax(t1, axis=0)  # 行最大值
#     2.np.argmin(t1, axis=1)  # 列最大值
# 2.创建一个全为0的数组：np.zeros((2, 4))
# 3.创建一个全为1的数组：np.ones((3, 5))
# 4.创建一个对角线为1的方阵

# copy和view
# 1.a=b,完全不复制，a和b相互影响
# 2.a=b[:],视图操作，一种切片，回创建新的对象a，但是a的数据完全由b保管，他们两个的数据变化是一致的
# 3.a=b.copy(),复制，a和b相互独立

# nan
# 1. np.nan == np.nan   # False
# 2. np.nan != np.nan   # True
# 3. np.count_nonzero(t!=t)  # 统计nan的个数
# 4. t2 != t2  # nan位置为true，其余为false
# 5. np.nisnan(t2) # 同上
# 6. np.count_nonzero(np.isnan(t2))  # 统计t2中nan的个数
# 7. nan与任何值计算都是nan
# 8. 含有nan的t，求和时np.sum(t),值为nan


# np.sum
# 1.np.sum(t)  # 全部求和
# 2. np.sum(t, axis=0)  #  按0轴求和，1轴上的所有数相加
# 3. np.sum(t, axis=1)  # 按1轴求和，0轴上的所有数相加

# 计算时，不能简单的把nan替换为0，这样的话平均值可能会变小
# 方法有，替换为平均值/中值/删除这一行

# numpy中常用的统计函数
# 求和：t1_data.sum(axis=None)
# 均值：t1_data.mean(axis=None)
# 中值：np.median(t1_data, axis=None)
# 最大值：t1_data.max(axis=None)
# 最小值：t1_data.min(axis=None)
# 极值：np.ptp(t1_data, axis=None)
# 标准差：t1_data.std(axis=None)
# 默认返回多维数组的全部统计结果，如果指定axis则返回一个当前轴上的结果

# t2.mean(axis=0)  # 中值
