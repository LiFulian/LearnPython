import socket  # 本代码为理解，无法运行， # 单进程／单线程　通过非阻塞实现检测多个套接字，
import time   # 加延时，看效果

tcp_server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_tcp.bind(("", 7899))
tcp_server_tcp.listen(128)
tcp_server_tcp.setblocking(False)  # 设置套接字为非阻塞

client_socket_list = list()

while True:
    time.sleep(1)

    try:
        new_socket, new_addr = tcp_server_tcp.accept()  # 非阻塞直接返回，可能为空
    except Exception as ret:
        print(ret)
        print("---没有新客户端到来---")
    else:
        print("---只要没有产生异常，那么意味着　来了一个新的客户端---")
        new_socket.setblocking(False)
        client_socket_list.append(new_socket)

    for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv(1024)
        except Exception as ret:
            print(ret)
            print("---这个客户端没有发来数据---")
        else:
            print("---客户端发送来了数据/可能为空---")
            print(recv_data)
            if recv_data:
                print("---对方未调用close---")
            else:
                client_socket.close()
                client_socket_list.remove(client_socket)  # 数据结构上优化，应使用列队
                print("客户端关闭---")


# 列表里面有１ｗ个，只有最后一个在链接时，前９９９９个应该删除
# 当列表里面的客户端服务过之后应该删除