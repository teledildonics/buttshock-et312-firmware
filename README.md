# Erosoutsider - ET-312 Firmware

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

## erosoutsider Implementations

If you are looking for a language specific version of the erosoutsider
work, each language has a repo assigned to it:

- Python Library - http://github.com/metafetish/erosoutsider-py
- Rust Library - http://github.com/metafetish/erosoutsider-rs
- Javascript Library for Node, Chrome Apps, and possibly for a general
  WebSerial API, should one ever exist -
  http://github.com/metafetish/erosoutsider-js
- Arduino Library - http://github.com/kinkyhacks/venerate

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

    Copyright (c) 2016, qDot
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:
        * Redistributions of source code must retain the above copyright
          notice, this list of conditions and the following disclaimer.
        * Redistributions in binary form must reproduce the above copyright
          notice, this list of conditions and the following disclaimer in the
          documentation and/or other materials provided with the distribution.
        * Neither the name of the Kyle Machulis/Nonpolynomial Labs nor the
          names of its contributors may be used to endorse or promote products
          derived from this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY qDot ''AS IS'' AND ANY EXPRESS OR
    IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED. IN NO EVENT SHALL Kyle Machulis/Nonpolynomial Labs
    BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
    EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
    TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
    ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
    TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
    THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
    SUCH DAMAGE

