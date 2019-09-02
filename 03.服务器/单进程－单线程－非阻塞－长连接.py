import socket
import re

# 浏览器中输入　http://127.0.0.1:6789/index1.html　　进行验证


def service_client(new_socket, request):
    """为这个客户端返回数据"""

    # １. 接收浏览器发送过来的请求，即http请求
    # GET /HTTP/1.1
    # ......
    # request = new_socket.recv(1024).decode("utf-8")

    request_lines = request.splitlines()
    # print(">" * 20)
    # print(request_lines)

    # GET /index.html HTTP/1.1
    # get post put del..
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        print("*"*20, file_name)
        if file_name == "/":
            file_name = "/index.html"

    # ２. 返回http格式的数据，给浏览器
    try:
        f = open("." + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "-----file not found-----"
        new_socket.send(response.encode("utf-8"))
    else:

        html_content = f.read()
        f.close()

        response_body = html_content

        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length: %d\r\n" % len(response_body)
        print("&"*10 + response_header)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body

        new_socket.send(response)
# 关闭套接
#     new_socket.close()


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 重启地址可使用

    # 2. 绑定
    tcp_server_socket.bind(("", 6789))

    # 3. 变为监听的套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)

    client_socket_list = list()
    while True:
        # 4. 等待新客户端的链接
        try:
            new_socket, client_addr = tcp_server_socket.accept()
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:  # 轮询的方式，没有epoll的时间通知效率高
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                # print(ret)
                pass
            else:
                if recv_data:
                    service_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
