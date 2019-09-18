import pandas as pd
data = pd.read_csv("./CA_videos.csv")
df = pd.DataFrame(data)
# print(data)
# print("*"*100)
# print(df.info)
# 取部分信息

temp = {"video_id": df["video_id"], "view_count": df["view_count"], "likes": df["likes"], "dislikes": df["dislikes"],
        "comment_count": df["comment_count"]}
df = pd.DataFrame(temp)

# dataFrame中的排序
df = df.sort_values(by="likes", ascending=True)

# pandas取行或者列的注意点
# - 方括号写数字表示取行，对行进行操作
# — 写字符串，表示的是取列索引，对列进行操作
# df[:100]["likes"]  # 同时取行和列

# 布尔索引
# &,|,不同条件之间使用（），对于字符串长度筛选可以使用.str.len() > 4
# print(df[df["likes"] > 10000])

print(df[(df["comment_count"] > 10000) & (df["likes"] > 20000)])

# print(df)
# df = pd.DataFrame(data_list)
# print(df)


# DataFram的基础属性
# df.shape  # 行数，列数
# df.dtypes  # 列数据类型
# df.ndim  # 数据维度
# df.index  # 行索引
# df.columns  # 列索引
# df.values  # 对象值，二维ndarrray数组
#
# # DataFrame整体情况查询
# df.head(3)
# df.tail(3)  # 返回头3行，默认5
# df.info()  # 行数，列数，类索引，列非空值个数，列类型，内存占用
# df.describe()  # 综合统计结果，计数，均值，标准差，最大值，四分位，最小值

# 缺失数据的处理
