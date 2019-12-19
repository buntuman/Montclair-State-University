from socket import *

#global variables
clientCount  = 0 # varible to keep track of the number of clients (Not neccessary)
serverPort = 5000 # the servers port number
serverSocket = socket(AF_INET, SOCK_STREAM) # create an IP4 socket connection
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


while True: # Infinite loop that accepts clients connections. Can only be terminated by the OS .
    clientCount += 1 # increment the client counter
    print("The server is ready to receive.")
    connectionSocket, addr = serverSocket.accept() # accept the connection from a client
    print("Currently Serving client number %d"%(clientCount))
    while True: # this loop servers on client only and exits if and only if the client sends a 'quit' message
        sentence = connectionSocket.recv(1024).decode()
        if(sentence.lower() == 'quit'):
            break
        else:
            capitalizedSentence = sentence.upper()
            connectionSocket.send(capitalizedSentence.encode())
    print("Clieent %d Requested server to quit. Bye Client %d"%(clientCount,clientCount))
d
