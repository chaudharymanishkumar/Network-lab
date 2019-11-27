#CRC sender 
#Client in server-client model
#MKChaudhary
import socket
def xor(a,b):
	result=[]
	for i in range(1,len(b)):
		if a[i] == b[i]:
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

def encodedata(data,key):
	appended_data=data+ '0'*(len(key) -1)
	remainder=mod2div(appended_data,key)
	codeword=data+remainder
	return codeword

s=socket.socket()
port=1234
s.connect(('127.0.0.1', port))
input_string = raw_input("Enter data you want to send->") 
data=(''.join(format(ord(x),'b')  for x in input_string))
print data
key=raw_input("Enter key: ")
ans=encodedata(data,key)
print ans
s.sendall(ans) 
print s.recv(1024) 
s.close() 

'''Program Execution
HP-Pavilion-Laptop-15-cc1xx:~/Desktop/cn$ python crc_sender.py 
Enter data you want to send->manish
110110111000011101110110100111100111101000
Enter key: 1001
110110111000011101110110100111100111101000100
THANK you Data ->110110111000011101110110100111100111101000100 Received No error FOUND
'''
