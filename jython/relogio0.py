#!/usr/bin/env jython
# coding: utf-8

from javax.swing import *
from java.awt import Font
from time import strftime

frame = JFrame(u'Relógio',
    defaultCloseOperation = JFrame.EXIT_ON_CLOSE)

rel = JLabel('00:00:00',font=Font('Sanserif',Font.BOLD,70))
frame.contentPane.add(rel)
frame.pack()
frame.visible = True

def tic(evento):
    agora = strftime('%H:%M:%S')
    if rel.text != agora:
        rel.text = agora

Timer(100, tic).start()

#from java.awt import *
#rel.foreground = Color.RED
