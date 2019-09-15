import numpy as np


def fill_ndarray(t1):
    for i in range(t1.shape[1]):  # 遍历每一列 替换为列平均值
        temp_col = t1[:, i]   # 当前的一列
        nan_num = np.count_nonzero(temp_col != temp_col)
        if nan_num != 0:  # 不为零，说明当前这一列有nan
            temp_not_nan_col = temp_col[temp_col == temp_col]  # 去掉nan
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()  # 替换
    return t1


if __name__ == "__main__":
    t1 = np.arange(12).reshape((3, 4)).astype("float")
    t1[1, 2:] = np.nan
    print(t1)
    t1 = fill_ndarray(t1)
    print(t1)

