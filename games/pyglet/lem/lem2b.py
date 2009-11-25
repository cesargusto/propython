#!/usr/bin/env python
# coding: utf-8

import pyglet

pyglet.resource.path = ['imagens']
pyglet.resource.reindex()

class Lem(pyglet.sprite.Sprite):
    def __init__(self):
        self.figura = pyglet.resource.image('lem.png')
        super(Lem, self).__init__(self.figura)
        self.x = 100
        self.y = 500
        
    def mover(self, dt):
        self.y -= 10
        
class PousoLunar(pyglet.window.Window):
    def __init__(self):
        super(PousoLunar, self).__init__(800, 600)
        self.fundo = pyglet.resource.image('earthrise800x600.jpg')
        self.lem = Lem()
        pyglet.clock.schedule_interval(self.lem.mover, 1/60.)

        pyglet.app.run()

    def on_draw(self):
        self.clear()
        self.fundo.blit(0, 0)
        self.lem.draw()
        
    def on_key_press(self, symbol, modifiers):
        self.lem.mover()
        
if __name__ == '__main__':
    PousoLunar()
