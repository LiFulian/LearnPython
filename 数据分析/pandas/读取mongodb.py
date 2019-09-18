from pymongo import MongoClient
import pandas as pd

# 默认链接本地mongodb（暂未配置）

client = MongoClient()
collection = client["douban"]["tv1"]
data = list(collection.find())

print(data)

df = pd.DataFrame(data)
print(df)

