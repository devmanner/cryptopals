

fp = open("chall8.txt", 'r')

blocks = {}

for l in fp.readlines():
    line = bytearray.fromhex(l)
    for i in range(len(line) // 16):
        block = line[i*16 : i*16+16].hex()
        if block in blocks:
            print("Block " + block + " is found a second time in line: " + line.hex())
        blocks[block] = line
        
