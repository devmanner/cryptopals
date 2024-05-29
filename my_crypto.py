from Crypto.Cipher import AES

def pkcs7_padding(s):
    block_size = 16 # bytes
    x = bytearray()
    x.extend(map(ord, s))

    print("String: " + s)
    print("Original length: " + str(len(x)))

    # Easier to understand...
    # if (len(x) % block_size) == 0:
    #     pad_size = 0
    # else:
    #     pad_size = block_size - (len(x) % block_size)

    # Cleaner but more difficult to interpret
    pad_size = (block_size - (len(x) % block_size)) % block_size

    x.extend([4] * pad_size)

    print(x.hex())
    print("Final length: " + str(len(x)))
    print("Padded: " + str(pad_size))

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
    clear_txt = bytearray(0)
    for i in range(len(cipher_txt) // crypt.block_size):
        encrypted_block = cipher_txt[i*crypt.block_size : i*crypt.block_size+crypt.block_size]
        plain_txt = xor(crypt.decrypt(encrypted_block), iv)
        clear_txt.extend(plain_txt)
        iv = encrypted_block
    return clear_txt
    
def aes_ecb_decrypt(key, cipher_txt):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(cipher_txt)
