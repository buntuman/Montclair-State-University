from socket import *

serverName = 'localhost'
serverPort = 5000

sentence = input("Enter Math Expression : ")
while sentence.lower() != 'quit':
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())
    clientSocket.close()
    sentence = input("Enter Math Expression : ")
