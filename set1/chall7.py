from Crypto.Cipher import AES
import base64 


key = "YELLOW SUBMARINE"

fp = open("chall7.txt", "r")
b64 = fp.read()
cipher_txt = base64.b64decode(b64)

cipher = AES.new(key, AES.MODE_ECB)

clear_txt = cipher.decrypt(cipher_txt)

print(clear_txt)
