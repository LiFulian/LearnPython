def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a  # 等待send
        print(">>>ret>>>", ret)
        a, b = b, a+b
        current_num += 1


obj = create_num(10)

# obj.send(None)  # send一般不会放到第一次启动生成器，如果非要这么做，那么传递None

ret = next(obj)
print(ret)

# send 里面的数据会传递给第５行，当做yield a 的结果，然后ret保存这个结果，，，
# send 的结果是下一次调用yield时yield后面的值
ret = obj.send("hhhh")
print(ret)