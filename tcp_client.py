import socket 
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务端
s.connect(("192.168.2.142", 6205))

# 请求 | 发送数据到服务端
# 253_18439422019_925 唯一索引
# 122518143 操作码，每次不一样
s.sendall(b'ul,253_18439422019_925,1,864294049954898,ios7.2,49.233.52.212,1,122518143\r\n')

# 响应 | 接受服务端返回到数据
#{
#    "Code":0,
#    "Content":{
#        "IsNew":1,
#        "Level":1,
#        "Name":"44Oq44O844OA44O85qeY",
#        "Port":2556,
#        "ServerIP":"192.168.2.142",
#        "Token":"784133cb0f80",
#        "UniqueId":"253_18439422019_925",
#        "UserId":"72340172821324839"
#    },
#    "Err":"",
#    "Sid":"122518143"
#}

# bytes 二进制字节序列
data = s.recv(1024)     
print(data) # hello

# str
strdata = data.decode(encoding='utf-8') 
print(type(strdata))
print(strdata)

# 取长度和消息体 len body
msglen  = int(strdata[:5], 16)  # 将字符串转换为整数，16进制
msgbody = strdata[5:]           # 消息体字符串
print(msglen)
print(len(msgbody))

if msglen != len(msgbody):
    print("data'len is wrong ...")
    pass

print(msgbody)

# json-->python
jsonobj = json.loads(msgbody)
print(type(jsonobj))

# python-->json 并且格式化
print(json.dumps(jsonobj, sort_keys=True, indent=4, separators=(',', ':')))

# 关闭 socket
s.close()
