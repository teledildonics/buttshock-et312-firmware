#!/usr/bin/python3
import argparse
import copy


class ET312FirmwareUtils(object):

    KEYS = [0x65, 0xed, 0x83]
    IV = [0xb9, 0xfe, 0x8f]

    def __init__(self, input_file, output_file=None):
        self.iv = copy.copy(ET312FirmwareUtils.IV)
        with open(input_file, "rb") as f:
            self.input_file = bytearray(f.read())
        self.fill_space()
        if output_file:
            self.output_file = open(output_file, "wb")

    def generate_crc(self):
        xor = 0
        add = 0
        for c in range(15872 - 16):
            xor ^= self.input_file[c]
            add += self.input_file[c]
        return [xor, (add & 0xff), ((add >> 8) & 0xff)]

    def encrypt(self, write_crc=True):
        funcs = {0: lambda x: ((x - 0x41 if x >= 0x41
                                else ((x - 0x41) + 0x100)) ^ 0x62) & 0xff,
                 1: lambda x: (x >> 4) | ((x & 0x0f) << 4),
                 2: lambda x: x}

        if write_crc:
            crc = self.generate_crc()
            for i in range(3):
                self.input_file[-16 + i] = crc[i]

        for i in range(0, len(self.input_file)):
            n = self.input_file[i]
            choice = i % 3
            output = funcs[choice](n ^ self.iv[choice] ^ self.KEYS[choice])
            self.output_file.write(bytearray([output]))
            self.iv[choice] = output

    def decrypt(self):
        funcs = {0: lambda x: ((x ^ 0x62) + 0x41) & 0xff,
                 1: lambda x: (n >> 4) | ((n & 0x0f) << 4),
                 2: lambda x: x}

        for i in range(0, len(self.input_file)):
            n = self.input_file[i]
            choice = i % 3
            output = funcs[choice](n) ^ self.iv[choice] ^ self.KEYS[choice]
            self.output_file.write(bytearray([output]))
            self.iv[choice] = n

    def fill_space(self):
        if len(self.input_file) >= 15872:
            return
        self.input_file += bytearray([0] * (15872 - len(self.input_file)))

    def upload(self, port):
        import serial
        from xmodem import XMODEM
        import io
        # In case xmodem starts acting up
        # import logging
        # logging.basicConfig(level=logging.DEBUG)

        s = serial.Serial(port, 19200, timeout=1,
                          parity=serial.PARITY_NONE,
                          bytesize=8, stopbits=1,
                          xonxoff=0, rtscts=0)

        def getc(size, timeout=1):
            return s.read(size)

        def putc(data, timeout=1):
            return s.write(data)

        modem = XMODEM(getc, putc)
        modem.send(io.BytesIO(self.input_file))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input_file",
                        help="File to take action on")
    parser.add_argument("-o", "--output", dest="output_file",
                        help="File to output, if needed by action")
    parser.add_argument("-d", "--decrypt", dest="decrypt", action="store_true",
                        help="Decrypt input file, store in output file")
    parser.add_argument("-e", "--encrypt", dest="encrypt", action="store_true",
                        help="Encrypt input file, store in output file."
                        " Adds checksum to output by default.")
    parser.add_argument("-u", "--upload", dest="upload",
                        help="Upload input file to box, expects com port as argument."
                        "(requires serial and xmodem packages)")
    parser.add_argument("-c", "--crc", dest="crc", action="store_true",
                        help="Output xor/checksum for input file")
    args = parser.parse_args()

    if not args.input_file:
        print("ERROR: Input file required to run.")
        parser.print_help()
        return 1

    if (args.decrypt or args.encrypt) and not args.output_file:
        print("ERROR: Output file required for encryption/decryption.")
        parser.print_help()
        return 1

    etfw = ET312FirmwareUtils(args.input_file, args.output_file)
    if args.encrypt:
        etfw.encrypt()
    elif args.decrypt:
        etfw.decrypt()
    elif args.upload:
        etfw.upload(args.upload)
    elif args.crc:
        print(["0x%.02x" % x for x in etfw.generate_crc()])
    return 0

if __name__ == "__main__":
    main()
