nums1 = [x*2 for x in range(10)]  # 返回的是列表，占用空间
nums2 = (x*2 for x in range(10))  # 返回的是生成器generator，存储生成方法，占用空间小
# ####################生成器是一种特殊的迭代器

# yield 记录执行位置，返回值，下次从此位置继续


def create_num(all_num):
    print("---1---")
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("---2---")
        # print(a)
        yield a  # 如果一个函数中有yield语句，那么这个就不在是函数，而是一个生成器的模板
        print("---3---")
        a, b = b, a+b
        current_num += 1
        print("----4----")


# 如果在调用create_num的时候，发现这个函数中有yield那么此时，不是调用函数，而是创建一个生成器对象
obj = create_num(10)

ret = next(obj)
print(ret)

ret = next(obj)
print(ret)

# for num in obj:
#     print(num)

