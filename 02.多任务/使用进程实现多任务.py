# .exe是一个可执行的二进制文件
# 程序是死的，运行起来之后叫进程（简单理解）
# 进程拥有资源，代码，网络，硬件，可以调动显卡，网卡，蓝牙，摄像头，等软硬件
# 并行：真的多任务
# 并发：假的多任务

# 进程状态：新建，就绪，等待，运行，死亡
# 进程相对独立，代码不复制，共享代码，耗费资源，进程数越多，进程单位被处理时间越少．
# 进程数增多，cpu核数＞最佳进程处理数时，效率增高，
# 能共享的共享，不能共享的不共享，（写时拷贝）

# 现有进程，再有线程，一个进程里面知识有一个主线程，还可以有一或多个子线程

# 优缺点：线程执行开销小，但不利于资源的保护和管理；进程相反．

# import threading
import time
import multiprocessing


def test1():
    while True:
        print("1....")
        time.sleep(1)


def test2():
    while True:
        print("2.....")
        time.sleep(1)


def main():
    # t1 = threading.Thread(target=test1)
    # t2 = threading.Thread(target=test2)
    # t1.start()
    # t2.start()

    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()



