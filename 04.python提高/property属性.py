"""经典类"""
# 私有属性配合公有方法，起到防护作用，python中有更好的方法


class Pager:
    def __init__(self, current_page):
        # 当用户请求的页码（第一页，第二页．．．）
        self.__current_page = current_page
        # 每页默认显示10条数据
        self.__per_items = 10

    @property
    def start(self):
        val = (self.__current_page - 1) * self.__per_items
        return val

    @property
    def end(self):
        val = self.__current_page * self.__per_items
        return val


p = Pager(2)
s = p.start
e = p.end  # 调用时类似属性，不需要(),省去考虑参数的问题
print(s, e)
