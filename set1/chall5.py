
input = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"

cipher = bytearray(len(input))
for i in range(len(input)):
    cipher[i] = ord(key[i % 3]) ^ ord(input[i])

print(cipher.hex())

