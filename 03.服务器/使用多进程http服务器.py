import socket
import multiprocessing
# 由于tcp有３次握手４次挥手，当本服务器关闭重启时会显示地址已占用（约两分钟）
# 加上一行代码可解决


def service_client(new_socket):
    """为这个客户端返回数据"""
    # 1.接收浏览器发送过来的请求，即http请求
    # GET / HTTP/1.1
    # ...
    request = new_socket.recv(1024)
    print(request)

    # 2. 返回http格式的数据，给浏览器
    # 2.1 组装发送给浏览器的数据－－header
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # 2.2 准备发送给浏览器的数据--body
    response +="<h1>好哈</h1>"
    new_socket.send(response.encode("gbk"))  # linux 为gbk,大多为utf-8

    # 关闭套接字
    new_socket.close()


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 重启地址可使用

    # 2. 绑定
    tcp_server_socket.bind(("", 6789))

    # 3. 变为监听的套接字
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        p = multiprocessing.Process(target=service_client, args=(new_socket,))
        p.start()

        new_socket.close()  # 关闭父线程的这个套接字，（子线程中以服务）

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()