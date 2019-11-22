# client server application simulating persistent TCP
#This program also utilizes multithreading 
from socket import *
import threading

'''
    This is accepts a socket connection(Socket) and clientID(Integer) as its arguments.
    The function then continiously accepts the specified clients messages until 'quit' is received.
    All received messages are converted to uppercase and sent back to the sender. 
'''
def serveClient(tcpConnectionSock,clientCount):
    print("Serving Client %d "%(clientCount))
    while True:
        sentence = tcpConnectionSock.recv(1024).decode()
        if(sentence.lower() == 'quit'):
            break
        else:
            capitalizedSentence = sentence.upper()
            tcpConnectionSock.send(capitalizedSentence.encode())
    print(" Client %d  Requested quit. Bye client %d :) "%(clientCount,clientCount))


'''
    The 'ServerThread' class describes the characteristic of a ServerThread Object.
    A ServerThread object can be instanciated by providing a socket connection object and ClientID number to the constructor.
    The ServerThread extends the threaing class which gives multi-threading functionality to the ServerThread object.
'''
class ServerThread(threading.Thread):
    def __init__(self,tcpConnectionSocket,clientNum):
        self.tcpConnectionSocket = tcpConnectionSocket
        self.clientNum = clientNum
        threading.Thread.__init__(self)

    def run(self):
        serveClient(self.tcpConnectionSocket,self.clientNum)

clientCount = 0
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    print("The server is ready to receive.")
    clientCount += 1 # client counter. Not neccessary. Its just for my own sanity. Lol
    connectionSocket, addr = serverSocket.accept()
    t = ServerThread(connectionSocket,clientCount)
    t.start()
connectionSocket.close()
