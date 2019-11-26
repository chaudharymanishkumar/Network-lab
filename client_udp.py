import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(('127.0.0.1',4444))
message=raw_input("Enter string: ")
client.sendto(message,('127.0.0.1',4444))
data,addr=client.recvfrom(1024)
print "Reversed Data: "+data
client.close()
