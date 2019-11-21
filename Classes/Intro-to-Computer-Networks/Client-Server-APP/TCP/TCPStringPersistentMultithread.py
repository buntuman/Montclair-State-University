from socket import *
import threading


def serveClient(tcpConnectionSock):
    while True:
        sentence = tcpConnectionSock.recv(1024).decode()
        if(sentence.lower() == 'quit'):
            break
        else:
            capitalizedSentence = sentence.upper()
            tcpConnectionSock.send(capitalizedSentence.encode())


class ServerThread(threading.Thread):
    def __init__(self,tcpConnectionSocket):
        self.tcpConnectionSocket = tcpConnectionSocket
        threading.Thread.__init__(self)

    def run(self):
        serveClient(self.tcpConnectionSocket)


serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    print("The server is ready to receive.")
    connectionSocket, addr = serverSocket.accept()
    t = ServerThread(connectionSocket)
    t.start()
connectionSocket.close()
