import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务端
s.connect(("192.168.2.142", 6205))

# 请求 | 发送数据到服务端
# 253_18439422019_925 唯一索引
# 122518143 操作码，每次不一样
s.sendall(b'ul,253_18439422019_925,1,864294049954898,ios7.2,49.233.52.212,1,122518143\r\n')

# 响应 | 接受服务端返回到数据
data = s.recv(1024)

print(data) # hello

# 关闭 socket
s.close()
