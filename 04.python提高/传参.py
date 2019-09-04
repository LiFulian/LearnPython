# *args存储多余的形参是个元祖， **kwargs储存关键字参数，是个字典
def test2(a, b, *args, **kwards):
    print("-------")
    print(a)
    print(b)
    print(args)
    print(kwards)


def test1(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

    test2(a, b, args, kwargs)
    test2(a, b, *args, kwargs)
    test2(a, b, *args, **kwargs)


test1(11, 22, 33, 44, 55, 66, name="lfl", age=19)


