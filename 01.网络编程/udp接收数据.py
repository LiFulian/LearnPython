import socket


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 2. 绑定一个本地信息
    localaddr = ("", 7788)
    udp_socket.bind(localaddr)  # 必须绑定自己的ip和port

    # 3. 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        # recv_data这个变量储存的是一个元组(b'数据',('ip',port))
        recv_msg = recv_data[0]  # 储存接收的数据
        send_addr = recv_data[1]  # 储存发送方的地址信息
        
        # 4. 打印接收到的数据
        # print(recv_data)
        print("%s:%s"%(str(send_addr), recv_msg.decode("utf-8")))
    # 5.关闭套接字
    udp_socket.close()
if __name__ == "__main__":
    main()
    
