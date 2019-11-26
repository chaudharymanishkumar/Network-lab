#multichat @client
#Remove comment from code if you want to add client collapse time 
#when server is localhost else change ip address of server
#MKchaudhary
import socket 
import sys 
import time
from thread import *
client=socket.socket() 
port=4448
client.connect(('127.0.0.1',port))
#time_started = time.time()
#timeout=10
while True:
	#if time.time() > time_started + timeout:   
	#	sys.exit()
	data=client.recv(1024)
	print "Server: "+data
	send_data=raw_input("Client: ")
	client.send(send_data)
client.close()
