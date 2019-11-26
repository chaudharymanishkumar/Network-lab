def railfence(plainText):
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
data=raw_input("Enter message:")
print(railfence(data))
