#coding:utf-8
'''
file:client.py
date:9/9/17 3:43 PM
author:lockey
email:lockey@123.com
desc:socket编程客户端，python3.6.2
'''
import socket,sys,datetime,time
HOST = '120.79.70.119'
PORT = 5000
ADDR =(HOST,PORT)
BUFSIZE = 1024

sock = socket.socket()
try:
    sock.connect(ADDR)
    print('have connected with server')

# while True:
    for i in range(10):
        data = str(i)+','+str(i/5)
        print(len(data))
        if 1==1:
            print('send1:',data)
            sock.sendall(data.encode('utf-8')) #不要用send()
            recv_data = 'ok'
            print('receive:',recv_data)
        else:
            sock.close()
            break
        time.sleep(1)
except Exception:
    print('error')
    sock.close()
    sys.exit()
