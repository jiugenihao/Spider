import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('localhost', 6999))
server_sock.listen(5)

#while True:
    conn, addr = server_sock.accept()
    print(conn, addr)

    #while True:
    try:
        data = conn.recv(1024)
        print("receive:", data.decode())
        conn.send(data.upper())
    except ConnectionResetError  as e:
        print("close 占线的连接")
        break
    pass

    conn.close()
    pass
