from socket import *

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
	message = input("Enter a math Expression : ")
	if(message == "quit"):
		break
	clientSocket.sendto(message.encode(), (serverName, serverPort))
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	print(modifiedMessage.decode())
clientSocket.close()
