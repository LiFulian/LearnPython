import socket
import re

# 浏览器中输入　http://127.0.0.1:6789/index1.html　　进行验证


def service_client(new_socket):
    """为这个客户端返回数据"""

    # １. 接收浏览器发送过来的请求，即http请求
    # GET /HTTP/1.1
    # ......
    request = new_socket.recv(1024).decode("utf-8")
    request_lines = request.splitlines()
    print(">" * 20)
    print(request_lines)

    # GET /index.html HTTP/1.1
    # get post put del..
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        # print("*"*20,file_name)
        if file_name == "/":
            file_name = "/index.html"

    # ２. 返回ｈｔｔｐ格式的数据，给浏览器
    try:
        f = open("." + file_name, "rb")
        # print(file_name)
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "-----file not found-----"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        new_socket.send(response.encode("utf-8"))
        new_socket.send(html_content)
    # 关闭套接
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
        service_client(new_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
