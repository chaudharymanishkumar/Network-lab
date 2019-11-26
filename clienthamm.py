import socket
s=socket.socket()
print("Socket is Successfully Created")

port=50042

s.connect(('127.0.0.1',port))
test=[0 for i in range(7)]

for i in range(0,7):
    message=s.recv(1)
    test[i]=message.decode()
    test[i]=int(test[i])

print("received data is:-")
print test


p1=test[6]^test[4]^test[2]^test[0]
p2=test[5]^test[4]^test[1]^test[0]
p4=test[3]^test[0]^test[1]^test[2]


p=(4*p4)+(2*p2)+(p1)

if(p==0):
    print("no error!!")
 
else:
    print("error at "+str(7-p+1)+" position.")
    if(test[7-p]==0):
        test[7-p]=1
    else:
        test[7-p]=0
        
print("corrected data is:-")
print test
s.close()


'''Socket is Successfully Created
received data is:-
[1, 0, 1, 0, 0, 0, 1]
error at 5 position.
corrected data is:-
[1, 0, 1, 0, 1, 0, 1]'''

