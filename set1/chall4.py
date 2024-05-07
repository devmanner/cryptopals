from string_analysis import *

fp = open("chall4.txt", 'r')

min_err = 999
best_guess = ""
best_key = 'X'

for line in fp.readlines():
    line = line.rstrip()
    guess = bytearray.fromhex(line)
    for char in string.ascii_lowercase + string.ascii_uppercase + string.digits + "!\"#€%&/()=?*-_.:,;<> ":
        decr = [chr(x ^ ord(char)) for x in guess]
#        decr = [chr(x ^ char) for x in guess]
        sc = string_characteristics(decr)
        err = char_match(sc)
        
        if err < min_err:
            min_err = err
            best_guess = "".join(decr)
            best_key = char

print("Best guess: " + best_guess)
print("Best key: " + best_key)
print("Min error: " + str(min_err))
