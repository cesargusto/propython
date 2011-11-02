#!/usr/bin/env python
# coding: utf-8

from struct import unpack
pipe = open('/dev/input/js0','r')
action = []
prev_action = [' '] * 8
line = 0
while 1:
    character = pipe.read(1)
    action.append(ord(character))
    if len(action) == 8:
        if line % 2:
            prev_action = action[:]
            action_strs = ['%02x' % c for i, c in enumerate(action)]
        else:
            action_strs = ['%02x' % c if c != prev_action[i]
                           else '  ' for i, c in enumerate(action)]
        if action[6] == 1:
            descr = 'button %s %s' % (action[7]+1,
                                      'press' if action[4] else 'release')
        elif action[6] == 2:
            n = unpack('h', chr(action[4]) + chr(action[5]))[0]
            descr = 'axis %s %s %d' % ('XYZ'[action[7]],
                                       '%02x.%02x' % (action[4], action[5]),
                                       n)
        else:
            descr = '?'

        print '%6d  :  %s --> %s' % (line, ' '.join(action_strs), descr)
        if not line % 2:
            print
        line += 1
        #sys.stdout.flush()
        action = []

