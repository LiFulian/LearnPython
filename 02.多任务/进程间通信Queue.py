# Queue 队列，先进先出，（管）
# Stack 栈，先进后出（桶）
# 多进程，可以用来解耦，耦合度：关联度；（越低越好）

import multiprocessing


def download_from_web(q):
    """模拟下载"""
    data = [11, 22, 33, 44]

    # 向队列中写入数据
    for temp in data:
        q.put(temp)
        print("已经将%d存入队列中--" % temp)


def analysis_data(q):
    """ 模拟数据处理"""
    waitting_analysis_data = list()

    # 从队列中获取数据
    while True:
        data = q.get()
        waitting_analysis_data.append(data)
        # 模拟数据处理
        print(waitting_analysis_data)
        if q.empty():
            break


def main():
    # 1.创建一个队列
    q = multiprocessing.Queue()  # 不写默认最大

    # 2.创建多个进程，将队列中的引用当做实参进行传递到里面
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
