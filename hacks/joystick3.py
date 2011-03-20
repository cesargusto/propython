#!/usr/bin/env python

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
            b0, b1, b2, b3, position, group, control = unpack('4BhBB',action) 
            
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
                n = position
                descr = '%s axis %d' % ('XYZ'[control], n)
            elif group == 0x81:
                descr = 'button %s present' % (control+1)
            elif group == 0x82:
                descr = 'axis %s present' % ('XYZ'[control])
            else:
                descr = '?'                   
            
            print '%6d  :  %s --> %s' % (line, ' '.join(action_strs), descr)
            line += 1
            action = ''

