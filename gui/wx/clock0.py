#!/usr/bin/env python

'''variant of clock.py without OnPaint event handling

the only difference is that it takes a second to draw the 
time for the first time
'''

import wx
import time
class ClockWindow(wx.Window):
    def __init__(self, parent):
        wx.Window.__init__(self, parent)
        self.timer = wx.Timer(self)                         # Creating the timer
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)   # Binding a timer event
        self.timer.Start(1000)                              # Setting time interval
                               
    def Draw(self, dc):
        '''Drawing current time'''
        t = time.localtime(time.time())
        st = time.strftime("%I:%M:%S", t)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(60, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w-tw)/2, (h)/2 - th/2)
                                   
    def OnTimer(self, evt):
        '''Displaying the time event handler'''
        dc = wx.BufferedDC(wx.ClientDC(self))
        self.Draw(dc)
                
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="wx.Timer")
        ClockWindow(self)
        
if __name__=='__main__':
    app = wx.PySimpleApp()
    frm = MyFrame()
    frm.Show()
    app.MainLoop()


