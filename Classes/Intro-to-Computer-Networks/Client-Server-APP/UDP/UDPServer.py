from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive.")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = str(eval(message.decode().upper()))
    print("Received %s from %s"%(str(message.decode()),str(clientAddress)))
    print("Sending response %s"%(str(modifiedMessage)))
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
