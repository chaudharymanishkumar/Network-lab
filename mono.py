#Mono Alphabatic substitution cipher
#MkChaudhary
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
inverse_monoalpha_cipher = {}
for key, value in monoalpha_cipher.iteritems():
    inverse_monoalpha_cipher[value] = key
message = raw_input("Enter the text:-")

encrypted_message = []
for letter in message:
    encrypted_message.append(monoalpha_cipher.get(letter, letter))
print(''.join(encrypted_message))

