#!/usr/bin/env jython
# coding: utf-8

from javax.swing import *
from java.awt import Font
from time import strftime

class Relogio(JFrame):
    def __init__(self):
        JFrame.__init__(self, u'Relógio',
            defaultCloseOperation = JFrame.DISPOSE_ON_CLOSE,
            size = (360,100))
        self.mostrador = JLabel('HH:MM:SS',
            font=Font('Sanserif',Font.BOLD, 70))
        self.contentPane.add(self.mostrador)
        def tic(evento=None):
            agora = strftime('%H:%M:%S')
            if self.mostrador.text != agora:
                self.mostrador.text = agora
        tic()
        self.visible = True
        Timer(100, tic).start()

if __name__=='__main__':
    rel = Relogio()

#from java.awt import *
#rel.mostrador.foreground = Color.RED
