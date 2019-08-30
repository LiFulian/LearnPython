import threading
import time

def test1(temp):
    print("in test1 befor =  " + str(temp))
    temp.append(3)
    print("in test1 temp = " + str(temp))


def test2(temp):
    print("int test2 temp = " + str(temp))


g_num = [1, 2]

def main():
    t1 = threading.Thread(target=test1, args=(g_num,))
    t2 = threading.Thread(target=test2, args=(g_num,))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("in main g_num = " + str(g_num))

if __name__ == '__main__':
    main()

