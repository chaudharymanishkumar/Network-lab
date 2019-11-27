#Railfence Encryption and decryption for single rail.
#MkChaudhary
#27Nov'19
import math
def railfence_encrypt(plainText):
	plainText = plainText.lower()
	cipherText = ""
	rail1 = ""
	rail2 = ""
	for i in range(len(plainText)):
		if i%2 == 0:
			rail1 += plainText[i]
	 	else:
			rail2 += plainText[i]

	cipherText = rail1 + rail2
	return cipherText


def railfence_decrypt(cipher):
	mid=int(math.ceil(len(cipher)/2))
	plaintext=""
	for i in range(mid):
		plaintext+=cipher[i]
		plaintext+=cipher[mid+i]
	return plaintext

data=raw_input("Enter message:")
cipher=railfence_encrypt(data)
print "Encryted Cipher:-"+cipher
print "Decrypted Data:- "+railfence_decrypt(cipher) 


''' output- 
HP-Pavilion-Laptop-15-cc1xx:~/Desktop/cn$ python railfence.py 
Enter message:manish
Encryted Cipher:-mnsaih
Decrypted Data:- manish'''
