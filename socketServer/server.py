#coding:utf-8
'''
file:client.py
date:9/9/17 3:43 PM
author:lockey
email:lockey@123.com
desc:socket编程服务器端，python3.6.2
'''
import pymysql
from socketserver import BaseRequestHandler, ThreadingTCPServer
import threading

db = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="ZJ12345689",database="sa_work")  #连接数据库
cursor = db.cursor()  #获取操作游标
#SQL插入语句

BUF_SIZE = 1024


class Handler(BaseRequestHandler):
    def handle(self):
        address, pid = self.client_address
        print('%s connected!' % address)
        while True:
            data = self.request.recv(BUF_SIZE)
            if len(data)  > 0:
                input_data = data.decode().split(',')
                print('收到=', input_data)
                try:
                    print(input_data[0])
                    a = int(input_data[0])
                    b = float(input_data[1])
                    print(a,b)
                    # 执行sql语句
                    cursor.execute("INSERT INTO sa_test_client_info (client_id,cpu_info) values ({},{})".format(a, b))
                    # 提交到数据库执行
                    db.commit()
                    print('插入成功')
                except:
                    # 如果发生错误则回滚
                    db.rollback()
                    print('插入错误')
                cur_thread = threading.current_thread()
                # response = '{}:{}'.format(cur_thread.ident,data)
                # self.request.sendall(response.encode('utf-8'))
                print('已回复')
            else:
                print('close')
                break


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 5000
    ADDR = (HOST, PORT)
    server = ThreadingTCPServer(ADDR, Handler)  #参数为监听地址和已建立连接的处理类
    print('listening')
    server.serve_forever()  #监听，建立好TCP连接后，为该连接创建新的socket和线程，并由处理类中的handle方法处理
