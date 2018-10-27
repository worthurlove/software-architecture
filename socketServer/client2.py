#coding=utf-8
#!/usr/bin/python

from socket import *

HOST = '120.79.70.119'
PORT = 5000
BUFSIZE = 65535
ADDR = (HOST, PORT)

welcomeStr = 'Welcome to 12.1 python socket server'

def fileWrite(record, fileName):
        with open(fileName, 'w') as logFile:
            for recordItem in record:
                logFile.write(recordItem)

def main():
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    fileDir = 'filePath/warnLogFile.txt'
    print ('Will connect 12.1 python socket server')
    data = 'hello'
    tcpCliSock.send(data)

    retDataAll = ''

    while True:
        retDataTmp = tcpCliSock.recv(BUFSIZE)
        if not retDataTmp:
            break
        if not len(retDataTmp):
            break
        print (retDataTmp)
        retDataAll = retDataAll + retDataTmp
    print ('end ')
    tcpCliSock.close()
    fileWrite(retDataAll, fileDir)

if __name__ == '__main__':
    main()