from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    print("The server is ready to receive.")
    connectionSocket, addr = serverSocket.accept()
    while True:
        sentence = connectionSocket.recv(1024).decode()
        if(sentence.lower() == 'quit'):
            break
        else:
            capitalizedSentence = sentence.upper()
            connectionSocket.send(capitalizedSentence.encode())
connectionSocket.close()
