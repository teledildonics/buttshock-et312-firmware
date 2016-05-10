# Buttshock - ET-312 Firmware

## Project Goals

This project exists to reverse engineer the Erostek ET-312
Electrostimulation Device Firmware. The last update of the box
firmware was 1.6 in 2004, and it still contains bugs and issues to
this day. Seeing as this box has been around for 16 years now, there
are probably hundreds of them around the world.

It's time to make them work better. You know, for shocking people in
the butt.

## Repo Contents

This repo contains the following:

- Firmware and Hardware Documentation (doc and datasheet directories)
- Copies of available firmware
- Source code and build files for new firmware versions

## Firmware Utility

In the scripts directory, there is a python script named fw-utils.py.
This utility allows users to encrypt/decrypt their own firmware, as
well as handling checksum calcuation.

### Downloading Firmware

Due to copyright, we cannot distribute firmware files with the
Buttshock repo. The python script has the capability to download them
from the web, making it easy to quickly retreive them and start
working.

```
scripts/fw-utils.py --downloadfw
```

This command will download the firmware, and place both encrypted and
unencrypted versions in the "firmware" directory.

### Encrypting/Decrypting Firmware

To decrypt the .upg files in the firmware directory, simply run

```
scripts/fw-utils.py --decrypt -i firmware/312-16.upg -o firmware/312-16-decrypted.bin
```

After the decrypted firmware has been changed, it can be encrypted
again using a similar comment with the --encrypt action.

```
scripts/fw-utils.py --encrypt -i firmware/312-16-decrypted.bin -o firmware/312-16-new.bin
```

This file can then be uploaded to the ET-312.

## Annotations

We are now working on annotating the output from the flash. For
disassembly, we are using a patched version of the avrdisas assembler
(http://www.johannes-bauer.com/mcus/avrdisas/).

The patched version of the assembler is available at

https://github.com/metafetish/avrdisas

Patches are on master, and include support for the 8/16-byte character
strings that the ET-312 firmware uses, as well as more opcodes than
are available in the 0.7.0 release of avrdisas.

Annotation happens via additions to the tags file in the annotations/
directory of this repo. To generate a new version of the annotated
disassembly, use the following command, with paths changed as needed
(this command assumes the avrdisas repo is next to this repo):

```
bin/avrdisas -a1 -o1 -c1 -p1 -l1 -mm16 -t../erosoutsider-et312-firmware/annotation/312-16-decrypted.tags ../erosoutsider-et312-firmware/firmware/312-16-decrypted.bin > 312-16-decrypted.hex
```

## Other Erosoutsider Projects

For more information on other Erosoutsider projects, including serial
control for various boxes and other firmware, please see the main
erosoutsider repo README at

https://github.com/metafetish/erosoutsider

## FAQ

### WHY?!

There's probably hundreds if not thousands of ET-312 boxes around the
world. We'd like them to work better.

### Why not just build a new, better box?

That's certainly a solution, and we've been contacted by multiple
people who are doing just that. While that's totally awesome, and we
might take a crack at doing that ourselves at some point, we'd also
like what's out there to work better than it does right now.

### Why not just reimplement the firmware from the ground up?

The idea is to provide a way to upgrade things without having to crack
the box open and replace the CPU completely. That's a time consuming
process not everyone can pull off. If we can just have people reflash
their box, it saves a lot of trouble for everyone involved.

## License

All original code and documentation for the Erosoutsider Firmware is
covered under the following BSD license:

    Copyright (c) 2016, The Buttshock Project
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:
        * Redistributions of source code must retain the above copyright
          notice, this list of conditions and the following disclaimer.
        * Redistributions in binary form must reproduce the above copyright
          notice, this list of conditions and the following disclaimer in the
          documentation and/or other materials provided with the distribution.
        * Neither the name of The Buttshock Project nor the names of
          its contributors may be used to endorse or promote products
          derived from this software without specific prior written
          permission.

    THIS SOFTWARE IS PROVIDED BY The Buttshock Project ''AS IS'' AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
    THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
    PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Kyle
    Machulis/Nonpolynomial Labs BE LIABLE FOR ANY DIRECT, INDIRECT,
    INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
    HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
    CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
    OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
    EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE

