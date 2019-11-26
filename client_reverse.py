import socket
import sys
client=socket.socket()
client.connect(('127.0.0.1',4444))
data=raw_input("Enter string: ")
#data=data[::-1]
client.send(data)
print "Reversed string: " + client.recv(1024)
