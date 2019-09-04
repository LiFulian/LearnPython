"""新式类"""


class Goods(object):
    """python3中默认继承object类,可不写，
        以python2. 3 执行此程序的结果不同，因为只有python3中才有@xxx.setter @xxx.deleter
    """
    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


obj = Goods()
obj.price            # 获取商品价格
obj.price = 200      # 修改商品原价
del obj.price        # 删除商品原价
