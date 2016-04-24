with open("312-16-decrypted.bin") as f:
    b = f.read(15872)

iv = [0xb9, 0xfe, 0x8f]
keys = [0x65, 0xed, 0x83]
g = open("312-16-encrypted.bin", "wb")
for i in range(0,len(b)):
    if i % 3 == 0:
        # TODO: Make this actually like, you know, work.
        n = ord(b[i])
        n2 = (((n^0x62) + 0x41) & 0xff)
        iv[0] = n2 ^ iv[0] ^ keys[0]
        g.write(chr(iv[0]))
    if i % 3 == 1:
        n = ord(b[i])
        # calculate
        iv[1] = n ^ iv[1] ^ keys[1]
        # swap nibbles of input
        iv[1] = ((iv[1] >> 4) | ((iv[1] & 0x0f) << 4))
        g.write(chr(iv[1]))
    if i % 3 == 2:
        iv[2] = ord(b[i]) ^ keys[2] ^ iv[2]
        g.write(chr(iv[2]))
