import string

from string_analysis import *
#from string_analysis import string_characteristics
#from string_analysis import char_match

#import codecs
# Make sure input is a binary
#input = codecs.encode("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

input = bytearray.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

best_string = "none"
best_err = 100
best_key = ''

for char in string.ascii_lowercase + string.ascii_uppercase + string.digits + "!\"#€%&/()=?*-_.:,;<> ":
    decr = [chr(inp ^ ord(char)) for inp in input]
    sc = string_characteristics(decr)
    if sc["all_printable"] == True:
        err = char_match(sc)
        print("".join(decr))
        print("Error: " + str(err))
        print("=========================")
        if err < best_err:
            best_err = err
            best_string = "".join(decr)
            best_key = char

print("Best guess: " + best_string + " used decription key: " + best_key)
