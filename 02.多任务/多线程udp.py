import socket
import threading


def rexv_msg(udp_socket):
    """接收数据并显示"""
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data[0].decode("gbk"))


def send_msg(udp_socket, dest_ip, dest_port):
    """发送数据"""
    while True:
        send_data = input("输入要发送的数据：")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def main():
    """完成整体"""

    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定本地信息
    udp_socket.bind(("", 7890))

    # 3. 获取对方的ip
    # dest_ip = input("请输入对方的ip:")
    # dest_port = int(input("请输入对方的port"))
    dest_ip = "172.20.151.18"
    dest_port = 9999

    # 4. 创建２个线程，去执行相应的功能
    t_recv = threading.Thread(target=rexv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))

    t_recv.start()
    t_send.start()


if __name__ == '__main__':
    main()


