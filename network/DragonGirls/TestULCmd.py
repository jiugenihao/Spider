import _thread
import time
import socket

def CreateSocketAndSend(name, strdata):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务端
    err = s.connect(("192.168.2.142", 6205))

    # 请求 | 发送数据到服务端
    #s.sendall(b'ul,253_18439422019_925,1,864294049954898,ios7.2,49.233.52.212,1,122518143\r\n')
    s.sendall(bytes(strdata, 'utf-8'))

    # 响应 | 接受服务端返回到数据
    data = s.recv(1024)

    print(data) # hello

if __name__ == "__main__":

    for i in range(1000):
        try:
            # 253_18439422019_925 唯一索引
            # 122518143 操作码，每次不一样
            name        = "T" + str(i)
            opt         = "ul"
            uniqueid    = "101_18439422019_92" + str(i)
            channel     = '101'
            deviceid    = 'f7b939bad3a14171e971c50bd8700f29054e26c9'
            devicetype  = "QjM2NU0uUE9XRVIuKEdpZ2FieXRlLlRlY2hub2xvZ3kuQ28uLi5MdGQuKQ=="
            ip          = "49.233.52.212"
            svrid       = '1'
            sid         = 100000000 + i
            strdata = opt + ',' + uniqueid + ',' + channel + ',' + deviceid + ',' + devicetype + ',' + ip + ',' + svrid + ',' + str(sid) + '\r\n'
            _thread.start_new_thread(CreateSocketAndSend, (name, strdata, ))
            pass
        except:
            pass
        pass

    while 1:
        pass
    pass
