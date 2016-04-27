#/usr/bin/python3
import argparse
import copy


class ET312FirmwareUtils(object):

    KEYS = [0x65, 0xed, 0x83]
    IV = [0xb9, 0xfe, 0x8f]

    def __init__(self, input_file, output_file=None):
        self.iv = copy.copy(ET312FirmwareUtils.IV)
        with open(input_file, "rb") as f:
            self.input_file = bytearray(f.read())
        if output_file:
            self.output_file = open(output_file, "wb")

    def generate_crc(self):
        xor = 0
        add = 0
        for c in range(len(self.input_file) - 16):
            xor ^= self.input_file[c]
            add += self.input_file[c]
        return [xor, (add & 0xff), ((add >> 8) & 0xff)]

    def encrypt(self, write_crc=True):
        funcs = {0: lambda x: ((x - 0x41 if x >= 0x41 else ((x - 0x41) + 0x100)) ^ 0x62) & 0xff,
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
            self.output_file.write(bytes([output]))
            self.iv[choice] = output

    def decrypt(self):
        funcs = {0: lambda x: ((x ^ 0x62) + 0x41) & 0xff,
                 1: lambda x: (n >> 4) | ((n & 0x0f) << 4),
                 2: lambda x: x}

        for i in range(0, len(self.input_file)):
            n = self.input_file[i]
            choice = i % 3
            output = funcs[choice](n) ^ self.iv[choice] ^ self.KEYS[choice]
            self.output_file.write(bytes([output]))
            self.iv[choice] = n

    def upload():
        pass


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
    parser.add_argument("-u", "--upload", dest="upload", action="store_true",
                        help="Upload input file to box (requires serial and xmodem packages)")
    parser.add_argument("-c", "--crc", dest="crc", action="store_true",
                        help="Output xor/checksum for input file")
    args = parser.parse_args()

    if not args.input_file:
        print("ERROR: ET-312 Firmware Utility requires an input file to run.")
        parser.print_help()
        return 1

    if (args.decrypt or args.encrypt) and not args.output_file:
        print("ERROR: ET-312 Firmware Utility requires an output file for encryption/decryption.")
        parser.print_help()
        return 1

    etfw = ET312FirmwareUtils(args.input_file, args.output_file)
    if args.encrypt:
        etfw.encrypt()
    elif args.decrypt:
        etfw.decrypt()

if __name__ == "__main__":
    main()
