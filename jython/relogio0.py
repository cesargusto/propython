#!/usr/bin/env jython
# coding: utf-8

from javax.swing import *
from time import strftime

frame = JFrame(u'Relógio',
    defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
    size = (200,100),
)

formato = '<html><center><font size="7">%s</font></center></html>'
rel = JLabel(formato)
frame.contentPane.add(rel)
frame.visible = True

def tic(evento):
    agora = formato % strftime('%H:%M:%S')
    if rel.text != agora:
        rel.text = agora

Timer(100, tic).start()

#from java.awt import *
#rel.setForeground(Color.RED)
