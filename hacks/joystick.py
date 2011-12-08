#!/usr/bin/env python
import sys
pipe = open('/dev/input/js0','r')
while 1:
    byte = pipe.read(1)
    sys.stdout.write(' %02x ' % ord(byte))
    sys.stdout.flush()
