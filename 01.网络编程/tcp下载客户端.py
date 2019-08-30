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
        # 3. 上传文件名
        download_file_name = input("请输入要下载的文件名字: ")
        tcp_scoket.send(download_file_name.encode("utf-8"))

        # 4.接收文件中的数据
        recv_data = tcp_scoket.recv(1024)  # 1024->1kb  1024*1024->1mb

        # 5.把数据写入一个文件中
        if recv_data:
            with open("[新]" + download_file_name, "wb") as f:
                f.write(recv_data)
                print("已为您下载" + download_file_name)
        else:
            print("未找到" + download_file_name)
        # 6.关闭套接字
        tcp_scoket.close()

if __name__ == "__main__":
    main()

