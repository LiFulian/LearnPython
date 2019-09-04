print("*****多继承使用类名.__init___发生的状态*****")


class Parent(object):
    def __init__(self, name, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接收参数
        print("parent的init开始被调用")
        self.name = name
        print("parent的init结束被调用")


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接收参数
        print("Son1的init开始被调用")
        self.age = age
        super().__init__(self, name, *args, **kwargs)
        print("Son1的init结束被调用")


class Son2(Parent):  # 为避免多继承报错，使用不定长参数，接收参数
    def __init__(self, name, gender, *args, **kwargs):
        print("Son２的init开始被调用")
        self.gender = gender
        super().__init__(self, name, *args, **kwargs)
        print("Son２的init结束被调用")


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print("Grandson的init开始被调用")
        # 多继承时，相当于使用类名.__init__方法，要把每个父类全部重写一遍
        # 而super只用一句话，执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因
        # super(Grandson, self).__init__(name, age, gender)
        super().__init__(self, name, age, gender)  # 会调用父类
        print("Grandson的init结束被调用")


print(Grandson.__mro__)  # 打印表现Grandson的super执行顺序，返回值是元祖，Ｃ３算法，保证执行一次


gs = Grandson("grandson", 12, "男")
print("姓名：", gs.name)
print("年龄：", gs.age)
print("性别：", gs.gender)

print("*****多继承使用类名.__init___发生的状态*****")