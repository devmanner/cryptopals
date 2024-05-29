import sys
sys.path.insert(1, '../')
from my_crypto import *
import base64 


iv = b'\x00' * AES.block_size
key = "YELLOW SUBMARINE"

fp = open("chall10.txt", "r")
b64 = fp.read()
cipher_txt = base64.b64decode(b64)

clear_txt = aes_cbc_decrypt(key, iv, cipher_txt)

print(clear_txt)



