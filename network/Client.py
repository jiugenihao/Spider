import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
err = client_sock.connect(("192.168.6.187", 2556))
print(err)

#while True:
    #client_sock.send(msg.encode("utf-8"))
client_sock.send(msg)
data = client_sock.recv(102400)
print("receive:", data.decode())
pass

client_sock.close()