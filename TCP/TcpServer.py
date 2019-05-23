from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
b = "Hello Client"
while True:
    print("waiting for")
    tcpCliSock,addr = tcpSerSock.accept()
    print("dasd",addr)
    print(tcpCliSock)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        print(data)
        if not data:
            break
        tcpCliSock.send(str.encode(b))

    tcpCliSock.close()
tcpSerSock.close()
