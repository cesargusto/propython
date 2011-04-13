#!/usr/bin/env python

'''
Chapter 20: Sockets and Server-Side Network Protocol Modules
Example 20-8. Asynchronous TCP echo server using asynchat
'''

import asyncore, asynchat, socket

class MainServerSocket(asyncore.dispatcher):
    def __init__(self, port):
        print 'initing MainServerSocket'
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(('',port))
        self.listen(5)
    def handle_accept(self):
        newSocket, address = self.accept( )
        print 'Connected from', address
        SecondaryServerSocket(newSocket)

class SecondaryServerSocket(asynchat.async_chat):
    def __init__(self, *args):
        print 'initing SecondaryServerSocket'
        asynchat.async_chat.__init__(self, *args)
        self.set_terminator('\n')
        self.data = []
    def collect_incoming_data(self, data):
        self.data.append(data)
    def found_terminator(self):
        self.push(''.join(self.data))
        self.data = []
    def handle_close(self):
        print 'Disconnected from', self.getpeername( )
        self.close( )

MainServerSocket(8881)
asyncore.loop( )
