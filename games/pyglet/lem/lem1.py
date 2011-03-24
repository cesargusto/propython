#!/usr/bin/env python
# coding: utf-8

'''
import pyglet

pyglet.resource.path = ['imagens']
pyglet.resource.reindex()

janela = pyglet.window.Window(800, 600)

image = pyglet.resource.image('earthrise800x600.jpg')

@janela.event #decorator
def on_draw():
    janela.clear()
    image.blit(0, 0)

pyglet.app.run()
'''
############################
import pyglet

pyglet.resource.path = ['imagens']
pyglet.resource.reindex()

class PousoLunar(pyglet.window.Window):
    def __init__(self):
        self.fundo = pyglet.resource.image('earthrise800x600.jpg')
        super(PousoLunar, self).__init__(800, 600)

    def on_draw(self):
        self.clear()
        self.fundo.blit(0, 0)

PousoLunar()        
pyglet.app.run()

