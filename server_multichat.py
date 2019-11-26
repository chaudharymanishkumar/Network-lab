#multichat @server
#focus on server to client communication.Here client to client communication is not possible
#MKChaudhary
import socket 
import sys 
from thread import *
server=socket.socket() 
IP_address = ""
Port = 4448
server.bind((IP_address, Port)) 
server.listen(100) 

def create_client(conn):
	while True:
		data=raw_input("Server: ")
		conn.send(data)
		final=conn.recv(1024)
		print "Client: "+final

while True:
	conn,addr=server.accept()
	start_new_thread(create_client,(conn,))
