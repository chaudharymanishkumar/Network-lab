#LZW compression and Decompression
#MKChaudhary
#26nov'19
print("encoding")
string=raw_input("enter string to compress:-")
codes = dict([(chr(x), x) for x in range(256)])
compressed_data = []       
code_count = 257
current_string = ""
for c in string:
    current_string = current_string + c
    if current_string not in codes:
        codes[current_string] = code_count
        compressed_data.append(codes[current_string[:-1]])
        code_count += 1
        current_string = c
compressed_data.append(codes[current_string])
print("compressed string is:-")
print(compressed_data)

print("decoding")
print("received string is:-")
############decompression
strings = dict([(x, chr(x)) for x in range(256)])
next_code = 257
decompressed_string = ""
previous_string = ""
for c in compressed_data:
    if c not in strings:
        strings[c] = previous_string + (previous_string[0])
    if not(len(previous_string) == 0):
        strings[next_code] = previous_string + (strings[c][0])
        next_code +=1
    decompressed_string += strings[c]
    previous_string = strings[c]
print("".join(str(compressed_data)))
print(decompressed_string)


'''Program Execution
HP-Pavilion-Laptop-15-cc1xx:~/Desktop/cn$ python lzw.py 
encoding
enter string to compress:-ababbabcababba
compressed string is:-
[97, 98, 257, 258, 98, 99, 257, 259, 97]
decoding
received string is:-
[97, 98, 257, 258, 98, 99, 257, 259, 97]
ababbabcababba
'''
