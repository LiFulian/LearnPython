class Test:
    def __init__(self, name):
        self.__name = name


a = Test("lfl")

# print(a.__name)  # 报错

print(a.__dict__)  # 查看ａ下面的所有属性，返回字典
print(a._Test__name)  # __name变形为

a.__name = "nnn"  # 会在ａ下添加一个__name属性
print(a.__dict__)
print(a.__name)

print(Test.__dict__)
# google 魔法属性，好多．．．实现列表，字典，切片
