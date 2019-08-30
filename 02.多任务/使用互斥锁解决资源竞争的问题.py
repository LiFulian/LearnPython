import threading
import time
# 可能会出现死锁的情况，（定时解锁）


# 定义一个全局变量
g_num = 0


def test1(num):
    global g_num
    # 上锁，　如果之前没有被上锁，那么此时会上锁成功
    # 如果需要的锁已经被使用，此时会堵塞在这里，直到这个锁被打开
    # 用锁方式１
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()  # 解锁

    # # 用锁方式２(频繁解锁，相当耗时)
    # for i in range(num):
    #     mutex.acquire()
    #     g_num += 1
    #     mutex.release()  # 解锁

    print("---in test1 g_num = %d" % g_num)


def test2(num):
    global g_num

    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()

    print("in test2 g_num = %d" % g_num)


# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test1, args=(3000000,))  # 资源竞争，数小的时候不明显
    t2 = threading.Thread(target=test2, args=(3000000,))

    t1.start()
    t2.start()

    # 等待上面的２个线程执行完毕
    time.sleep(2)

    print("in main g_num = %d" % g_num)


if __name__ == '__main__':
    main()