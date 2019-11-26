import socket
import random
s=socket.socket()
print("Socket is Successfully Created")

port=50042

s.bind(('',port))
print("Socket is binded to %s" %(port))

s.listen(5)

print("Socket is listening")

print("Enter the 4 bit data")
a=[0 for i in range(7)]
for i in range(0,3):
    a[i]=int(input("enter bit"+str(i+1)+":-"))
a[4]=int(input("enter bit 4:-"))

a[6]=a[4]^a[2]^a[0]
a[5]=a[4]^a[1]^a[0]
a[3]=a[0]^a[1]^a[2]

print("The data to be sent is ")
print a

a[random.randint(0,len(a)-1)]=random.randint(0,1)
print("The data with error ")
print a

while True:
    try: 
    	c,addr=s.accept()
    	print("Got the connection from ",addr)
    	for i in range(0,7):
    	    a[i]=str(a[i])
    	    c.sendall(a[i])
    	c.close()
    except KeyboardInterrupt:
	print "server closing"
	c.close()
	break

'''
Socket is Successfully Created
Socket is binded to 50042
Socket is listening
Enter the 4 bit data
enter bit1:-1
enter bit2:-0
enter bit3:-1
enter bit 4:-1
The data to be sent is 
[1, 0, 1, 0, 1, 0, 1]
The data with error 
[1, 0, 1, 0, 0, 0, 1]
('Got the connection from ', ('127.0.0.1', 60020))
^Cserving closing'''

