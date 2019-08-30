import time
from collections import Iterable
from collections import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象成为一个可迭代的对象，（可以使用for),那么必须实现__iter__方法"""
        return self  # 返回一个含有__next__的可迭代对象，执行__next__方法，可以是自己(需要还是含有__next__)

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()
classmate.add("老王")
classmate.add("小张")
classmate.add("李四")

# print("判断classmate是否是可以迭代的对象：", isinstance(classmate, Iterator))
# classmate_iterator = iter(classmate)
# print("判断classmate_iterator是否是迭代器：", isinstance(classmate_iterator, Iterator))
# print(next(classmate_iterator))

for name in classmate:
    print(name)


