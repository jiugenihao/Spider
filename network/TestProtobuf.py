import Login_pb2
import sys


msg = Login_pb2.MceAuth()
msg.uniqueid = "1"
msg.accounttype = 1
msg.serverid = 91

print(msg)
sendDataStr = msg.SerializeToString()
print(sendDataStr)
