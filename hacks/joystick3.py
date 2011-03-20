#!/usr/bin/env python
# coding: utf-8

'''
Read events from a Microsoft SideWinder USB joystick, classic model with
8 buttons and a throttle (Z axis in this driver)
'''

from struct import unpack
pipe = open('/dev/input/js0','r')
action = ''
prev_action = ' ' * 8
prev_group_control = (0,0)
line = 0
while 1:
    for character in pipe.read(1):
        action += character
        if len(action) == 8:
            timestamp, position, group, control = unpack('ihBB',action)

            if prev_group_control != (group, control):
                print
                prev_group_control = (group, control)

            action_strs = ['%02x' % ord(c) if c != prev_action[i]
                               else '  ' for i, c in enumerate(action)]
            prev_action = action[:]
            if group == 1:
                descr = 'button %s %s' % (control+1,
                                          'press' if position else 'release')
            elif group == 2:
                descr = '%s axis %d' % ('XYZ'[control], position)
            elif group == 0x81:
                descr = 'button %s present' % (control+1)
            elif group == 0x82:
                descr = 'axis %s present; position %d' % ('XYZ'[control], position)
            else:
                descr = '?'

            print '%6d  %8d : %s --> %s' % (line, timestamp, ' '.join(action_strs), descr)
            line += 1
            action = ''

