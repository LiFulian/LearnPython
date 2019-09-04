print("*****多继承使用类名.__init___发生的状态*****")
class Parent(object):
	def __init__(self, name):
		print("parent的init开始被调用")
		self.name = name
		print("parent的init结束被调用")


class Son1(Parent):
	def __init__(self, name, age):
		print("Son1的init开始被调用")
		self.age = age
		Parent.__init__(self, name)
		print("Son1的init结束被调用")


class Son2(Parent):
	def __init__(self, name, gender):
		print("Son２的init开始被调用")
		self.gender = gender
		Parent.__init__(self, name)
		print("Son２的init结束被调用")
				

class Grandson(Son1, Son2):
	def __init__(self, name, age, gender):
		print("Grandson的init开始被调用")
		Son1.__init__(self, name, age)  # 会调用父类
		Son2.__init__(self, name, gender)  # 会调用父类
		print("Grandson的init结束被调用")  # 一共调用两次父类，浪费资源，缺点大


gs = Grandson("grandson", 12, "男")
print("姓名：", gs.name)
print("年龄：", gs.age)
print("性别：", gs.gender)


print("*****多继承使用类名.__init___发生的状态*****")