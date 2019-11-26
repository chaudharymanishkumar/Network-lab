monoalpha_cipher = {
    'a': 'm',
    'b': 'n',
    'c': 'b',
    'd': 'v',
    'e': 'c',
    'f': 'x',
    'g': 'z',
    'h': 'a',
    'i': 's',
    'j': 'd',
    'k': 'f',
    'l': 'g',
    'm': 'h',
    'n': 'j',
    'o': 'k',
    'p': 'l',
    'q': 'p',
    'r': 'o',
    's': 'i',
    't': 'u',
    'u': 'y',
    'v': 't',
    'w': 'r',
    'x': 'e',
    'y': 'w',
    'z': 'q',
    ' ': ' ',
}
def encryption(message):
	encrypted_message=[]
	for letter in message:
		encrypted_message.append(monoalpha_cipher.get(letter,letter))
	return ''.join(encrypted_message)

def decryption(message):
	decrypted_message=[]
	inverse_monoalpha_cipher={}
	for key,value in monoalpha_cipher.iteritems():
		inverse_monoalpha_cipher[value]=key
	for letter in message:
		decrypted_message.append(inverse_monoalpha_cipher.get(letter,letter))
	return ''.join(decrypted_message)

message = raw_input("Enter the text:-")
en_data=encryption(message)
print en_data
print decryption(en_data)

