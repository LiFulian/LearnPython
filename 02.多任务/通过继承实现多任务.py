import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + ' @ ' + str(i)  # name属性中保存当前线程的名字
            print(msg)


if __name__ == '__main__':
    t = MyThread()
    t.start()  # 自动调用里面的run
    time.sleep(2)
    print("当前运行线程" + str(threading.enumerate()))
