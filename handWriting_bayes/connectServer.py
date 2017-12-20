# client
import socket

server_ip = '0.0.0.0'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, 6463))
# 建立连接:
data = '一次价值xxx元王牌项目；可充值xxx元店内项目卡一张；可以参与V动好生活百分百抽奖机会一次！预约电话：xxxxxxxxxxx'
s.send(data)
# 发送数据:
print(s.recv(1024))
s.close()
