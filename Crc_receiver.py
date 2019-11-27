#CRC receiver 
#Server in server-client model
#MKChaudhary
import socket
def xor(a,b):
	result=[]
	for i in range(1,len(b)):
		if a[i]== b[i]:
			result.append('0')
		else:
			result.append('1')
	return ''.join(result)

def mod2div(divident,divisor):
	pick=len(divisor)
	temp=divident[0:pick]
	while pick < len(divident):
		if temp[0] == '1':
			temp=xor(divisor,temp) + divident[pick]
		else:
			temp=xor('0'*pick,temp) + divident[pick]
		pick+=1

	if temp[0]=='1':
		temp=xor(divisor,temp)
	else:
		temp=xor('0'*pick,temp)
	checkword=temp
	return checkword

def decodedata(data,key):
	remainder=mod2div(data,key)
	return remainder

s=socket.socket()
print ("Socket successfully created")
port=1234
s.bind(('', port))
print ("socket binded to %s" % (port)) 
s.listen(5) 
print ("socket is listening") 
while True: 
	try:
	    c, addr = s.accept() 
	    print('Got connection from', addr) 
	    data = c.recv(1024) 
	    print(data) 
	    if not data: 
		break
	    key = raw_input("Enter key: ")
	  
	    ans = decodedata(data, key) 
	    print("Remainder after decoding is->"+ans)  
	    temp = "0" * (len(key) - 1) 
	    if ans == temp: 
		c.sendall("THANK you Data ->"+data + " Received No error FOUND") 
	    else: 
		c.sendall("Error in data") 
	  
	except KeyboardInterrupt:
		print "server closing"
		c.close()
		break

		
'''Program Execution
HP-Pavilion-Laptop-15-cc1xx:~/Desktop/cn$ python crc_receiver.py 
Socket successfully created
socket binded to 1234
socket is listening
('Got connection from', ('127.0.0.1', 44630))
110110111000011101110110100111100111101000100
Enter key: 1001
Remainder after decoding is->000
'''
