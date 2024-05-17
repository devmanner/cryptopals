from Crypto.Cipher import AES
import base64 

def xor(x, y):
    if len(x) != len(y):
        print("XOR two byte arrays of unequal size!")
        print(x.hex())
        print(y.hex())
        exit()

    r = bytearray(0)
    for i in range(len(x)):
        r.append(x[i] ^ y[i])
    return bytes(r)

def aes_cbc_decrypt(key, iv, cipher_txt):
    crypt = AES.new(key, AES.MODE_ECB)
    #iv = init_vector
    clear_txt = bytearray(0)
    for i in range(len(cipher_txt) // crypt.block_size):
#        s1 = xor(iv, cipher_txt[i*crypt.block_size : i*crypt.block_size+crypt.block_size])
#        plain_txt = crypt.decrypt(s1)
        encrypted_block = cipher_txt[i*crypt.block_size : i*crypt.block_size+crypt.block_size]
        plain_txt = xor(crypt.decrypt(encrypted_block), iv)
        clear_txt.extend(plain_txt)
        iv = encrypted_block
    return clear_txt


iv = b'\x00' * AES.block_size
key = "YELLOW SUBMARINE"

fp = open("chall10.txt", "r")
b64 = fp.read()
cipher_txt = base64.b64decode(b64)

clear_txt = aes_cbc_decrypt(key, iv, cipher_txt)

print(clear_txt)



