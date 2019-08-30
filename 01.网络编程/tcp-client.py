import socket


def main():
    # 1. 创建tcp的套接字
    tcp_scoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.链接服务器
    server_ip = input("请输入要连接的服务器的ip:")
    server_port = int(input("请输入要链接的服务器的port:"))
    server_addr = (server_ip, server_port)
    tcp_scoket.connect(server_addr)
    while True:
        # 3. 发送数据/接收数据
        send_data = input("请输入要发送的数据:")
        tcp_scoket.send(send_data.encode("utf-8"))

        print(tcp_scoket.recv(1024).decode("utf-8"))

    # 4. 关闭套接字
    tcp_scoket.close()

if __name__ == "__main__":
    main()

