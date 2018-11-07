#coding:utf-8
'''
client1模拟客户端1
'''
import socket,sys,datetime,time,random
HOST = 'localhost'
PORT = 5000
ADDR =(HOST,PORT)
BUFSIZE = 1024

sock = socket.socket()
try:
    sock.connect(ADDR)
    print('have connected with server')

    while True:
        time_insert=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cpu_percent = random.random()
        data = str(cpu_percent)+','+str(time_insert)+',1'
        print(len(data))
        if 1==1:
            print('send1:',data)
            sock.sendall(data.encode('utf-8')) #不要用send()
            recv_data = 'ok'
            print('receive:',recv_data)
        else:
            sock.close()
            # break
        time.sleep(1)
except Exception:
    print('error')
    sock.close()
    sys.exit()
