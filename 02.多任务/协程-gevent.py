# 遇到延时就切换
# 协程依赖线程，线程依赖进程．
# 协程只有一个线程，延时时切换
# 最佳

import gevent
import time
from gevent import monkey  # gevent 补丁，保证原来的time.sleep,socket,等不用替换

monkey.patch_all()  # 补丁


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)


print("---1---")
g1 = gevent.spawn(f1, 5)

# gevent.sleep(10)  # ,这段时间主线程不能往下走,因为此时gevent里面暂时只有g1

print("---2---")
g2 = gevent.spawn(f2, 5)

print("---3---")
g3 = gevent.spawn(f3, 5)

# g1.join()
# g2.join()
# g3.join()
gevent.joinall([
    g1, g2, g3
])

