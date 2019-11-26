import math
def encryptMessage(msg):
	cipher=""
	k_idx=0
	msg_len=float(len(msg))
	msg_lst=list(msg)
	key_lst=sorted(list(key))
	col=len(key)
	row=int(math.ceil(msg_len/col))
	null_fill=int(row*col - msg_len)
	msg_lst.extend('_'*null_fill)
	matrix=[msg_lst[i:i+col] for i in range(0,len(msg_lst),col)]
	for _ in range(col):
		curr_idx=key.index(key_lst[k_idx])
		cipher+=''.join([row[curr_idx] for row in matrix])
		k_idx+=1
	return cipher

def decryptMessage(cipher):
	msg=""
	k_idx=0
	msg_idx=0
	msg_len=float(len(cipher))
	key_lst=sorted(list(key))
	msg_lst=list(cipher)
	col=len(key)
	row=int(math.ceil(msg_len/col))
	dec_cipher=[]
	for _ in range(row):
		dec_cipher+=[[None]*col]
	for _ in range(col):
		curr_idx=key.index(key_lst[k_idx])
		for j in range(row):
			dec_cipher[j][curr_idx]=msg_lst[msg_idx]
			msg_idx+=1
		k_idx+=1
	msg=''.join(sum(dec_cipher,[]))
	null_count=msg.count('_')
	if null_count>0:
		return msg[:-null_count]
	return msg

key = raw_input("Enter key : ")
plain_text = raw_input("Enter input plain text : ")
cipher_text = encryptMessage(plain_text)
decrypt_text = decryptMessage(cipher_text)

print("PLAIN TEXT : "+plain_text)
print("CIPHER TEXT : "+cipher_text)
print("DECRYPT TEXT : "+decrypt_text)
