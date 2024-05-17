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

    