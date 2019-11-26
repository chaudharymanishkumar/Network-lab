import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('',4444))
while True:
	data,addr=server.recvfrom(1024)
	print "Data received: "+data
	server.sendto(data[::-1],(addr[0],addr[1]))

server.close()	
