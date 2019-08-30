def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a  # 如果一个函数中有yield语句，那么这个就不在是一个函数，而是一个生成器的模板
        a, b = b, a + b
        current_num += 1
    return "over..."  # 在抛出错误时作为返回值


obj2 = create_num(30)
# 多个的话，互不影响

while True:
    try:
        ret = next(obj2)
        print(ret)
    except Exception as ret:
        print(ret.value)  # 这里是上面的"over..."
        break