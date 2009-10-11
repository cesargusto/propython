#!/usr/bin/env python
# coding: utf-8

import pyglet
from pyglet.window import key
from vetor import Vetor as V

pyglet.resource.path = ['imagens']
pyglet.resource.reindex()

class Lem(pyglet.sprite.Sprite):
    def __init__(self):
        self.figura = pyglet.resource.image('lem.png')
        self.vel = V(0, 0)
        super(Lem, self).__init__(self.figura, 100, 500)
        
    def acelerar(self, acel):
        self.vel = self.vel + acel

    def update(self, dt):
        self.x += self.vel.x
        self.y += self.vel.y
        

class PousoLunar(pyglet.window.Window):
    def __init__(self):
        super(PousoLunar, self).__init__(800, 600)
        self.fundo = pyglet.resource.image('earthrise800x600.jpg')
        self.lem = Lem()
        pyglet.clock.schedule_interval(self.lem.update, 1/60.)
        pyglet.app.run()

    def on_draw(self):
        self.clear()
        self.fundo.blit(0, 0)
        self.lem.draw()
                
    def on_key_press(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.lem.acelerar(V(1,0))
        elif symbol == key.LEFT:
            self.lem.acelerar(V(-1,0))
        elif symbol == key.UP:
            self.lem.acelerar(V(0,1))
        elif symbol == key.DOWN:
            self.lem.acelerar(V(0,-1))

if __name__ == '__main__':
    PousoLunar()
