#!/usr/bin/env python

from urllib2 import urlopen, HTTPError

BASE_URL = ('''http://ichart.finance.yahoo.com/table.csv?'''
            '''s={symbol}&a=11&b=01&c={year}&d=11&e=31&f={year}&g=m''')
            
symbols = ['AAPL', 'GOOG', 'FAKE', 'IBM', 'MSFT']

for sym in symbols:
    try:
        print urlopen(BASE_URL.format(symbol=sym, year=2010)).read()
    except HTTPError:
        print sym + '???'
        