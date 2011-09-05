#!/usr/bin/env python

import cgitb
cgitb.enable()

from datetime import datetime
print 'Content-Type: text/html;charset=utf-8'
print 'Refresh: 1'
print 
print '<h1>%s</h1>' % datetime.now().strftime('%H:%M:%S')

