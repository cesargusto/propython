#!/usr/bin/env python
# coding: utf-8

import pyglet


class Lem(pyglet.sprite.Sprite):
    def __init__(self):
        self.figura = pyglet.resource.image('lem.png')
        super(Lem, self).__init__(self.figura, 100, 500)

class PousoLunar(pyglet.window.Window):
    def __init__(self):
        super(PousoLunar, self).__init__(800, 600)
        self.fundo = pyglet.resource.image('earthrise800x600.jpg')
        self.lem = Lem()
        pyglet.app.run()

    def on_draw(self):
        self.clear()
        self.fundo.blit(0, 0)
        self.lem.draw()
        

if __name__ == '__main__':
    PousoLunar()
