import socket
import sys
server=socket.socket()
server.bind(('',4444))
server.listen(5)
while True:
	conn,addr=server.accept()
	data=conn.recv(1024)
	print data
	conn.send(data[::-1])
	
