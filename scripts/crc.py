with open("312-16-decrypted-changed.bin") as f:
    b = f.read()
xor = 0
add = 0
for c in range(len(b) - 16):
    xor ^= ord(b[c])
    add += ord(b[c])
print "0x%.02x 0x%.02x 0x%.02x" % (xor, (add & 0xff), ((add >> 8) & 0xff))

