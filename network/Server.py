import socket

LISTEN_NUM = 5
BUFSIZE = 1024
ip_port = ('localhost', 6999)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6999
server_sock.bind((host, port))
#server_sock.bind(ip_port)
server_sock.listen(LISTEN_NUM)

while True:
    conn, cli_addr = server_sock.accept()
    print("连接地址：%s" % str(cli_addr))
    #print(conn, cli_addr)

    #while True:
    try:
        data = conn.recv(BUFSIZE)
        print("receive:", data.decode())
        conn.send(data.upper())
    except ConnectionResetError  as e:
        print("close 占线的连接")
        break
    pass

    conn.close()
    pass
