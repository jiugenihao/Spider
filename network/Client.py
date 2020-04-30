import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(("localhost", 6999))

#while True:
msg = "test connect server"
client_sock.send(msg.encode("utf-8"))
data = client_sock.recv(1024)
print("receive:", data.decode())
pass

client_sock.close()