from socket import *

HOST = "139.180.130.113"
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = "Hello Sever"
    tcpCliSock.send(str.encode(data))
    b = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(b)

tcpCliSock.close()

