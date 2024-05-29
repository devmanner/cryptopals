import base64 
import sys
sys.path.insert(1, '../')
from my_crypto import *

key = "YELLOW SUBMARINE"

fp = open("chall7.txt", "r")
b64 = fp.read()
cipher_txt = base64.b64decode(b64)

clear_txt = aes_ecb_decrypt(key, cipher_txt)

print(clear_txt)
