with open("312-16.upg") as f:
    b = f.read(15872)

iv = [0xb9, 0xfe, 0x8f]
keys = [0x65, 0xed, 0x83]
g = open("d16.bin", "wb")
for i in range(0,len(b)):
    if i % 3 == 0:
        n = ord(b[i])
        n2 = (((n^0x62) + 0x41) & 0xff)
        g.write(chr(n2 ^ iv[0] ^ keys[0]))
        iv[0] = ord(b[i])
    if i % 3 == 1:
        # swap nibbles of input
        n = ord(b[i])
        n2 = (n >> 4) | ((n & 0x0f) << 4)
        g.write(chr(n2 ^ iv[1] ^ keys[1]))
        iv[1] = ord(b[i])
    if i % 3 == 2:
        g.write(chr(ord(b[i]) ^ keys[2] ^ iv[2]))
        iv[2] = ord(b[i])
