#!/usr/bin/env python

'''
Adapted by Luciano Ramalho from the example on page 539
of Alex Martelli's Python in a Nutshell, 2nd ed.
'''

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8881))
print "Connected to server"

def console():
    while True:
        line = raw_input('?> ')
        if not line.strip():
            resp = raw_input('quit? [y]/n ')
            if resp.strip() in 'Yy':
                break
        else:
            yield line

for line in console():
    sock.sendall(line+'\n')
    response = sock.recv(8192)
    print "R:", response
sock.close()
