import socket
import sys
import time

s = socket.socket()
host = input(str("Please enter the host name of the server: "))
port = 8080
s.connect((host, port))
print("Connected to chat server")
while 1:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print(" Server: ",incoming_message) 
        print("")
        kmessage = input(str(">>"))
        message = message.encode()
        s.send(message)
        print("message has been sent...")
        print("")
