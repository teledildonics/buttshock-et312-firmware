f = open("writedata.csv", "r")
b = open("fw.bin", "wb")
while True:
    l = f.readline()
    if l is None or len(l) == 0:
        break
    print l
    b.write(chr(int(l, 16)))
f.close()
b.close()
