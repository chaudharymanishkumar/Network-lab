#multichat @client
import socket 
import sys 
import time
from thread import *
client=socket.socket() 
client.connect(('127.0.0.1',4448))
time_started = time.time()
timeout=10
while True:
	#if time.time() > time_started + timeout:
	#	sys.exit()
	data=client.recv(1024)
	print "Server: "+data
	send_data=raw_input("Client: ")
	client.send(send_data)
