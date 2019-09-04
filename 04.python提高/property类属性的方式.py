class Foo(object):
    def get_bar(self):
        return "lfl"

    BAR = property(get_bar)  # 传引用


obj = Foo()
result = obj.BAR  # 自动调用get_bar方法，并获取方法的返回值
print(result)


"""property中的四个参数：详情google
方法名（对象.属性时调用）,
方法名（对象.属性=xxx时调用）,
方法名（del对象.属性时调用）,
字符串（对象.属性.__doc__时调用该属性的描述信息"""


# Django 中就有使用

