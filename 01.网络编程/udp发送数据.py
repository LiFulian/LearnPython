import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息,不写的话,系统随机分配
    udp_socket.bind(('', 7890))

    while True:
        # 从键盘获取数据
        send_data = input("请输入要发送的数据(输入'exit'结束:)")

        # 如果输入的数据是exit, 那么就退出程序
        if send_data == "exit":
            break

        # 可以使用套接字收发数据需要目标地址
        udp_socket.sendto(send_data.encode("utf-8"), ("172.20.151.18", 7788))

    #关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()

