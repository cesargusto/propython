#!/usr/bin/env/python
"""
How to convert an ISO-8601 date string to the miliseconds from the epoch
integer required by the Extended JSON format used by MongoDB [1]

[1] http://www.mongodb.org/display/DOCS/Mongo+Extended+JSON
"""

import calendar
from datetime import datetime

# ISO-8601 format extended to include fractions of seconds
# used by OpenLibrary JSON dumps
ISO_8601 = '%Y-%m-%dT%H:%M:%S'
ISO_8601_EXTENDED = ISO_8601 + '.%f'

# (0) start with a an extended date string
dt_str = '2008-04-01T03:28:50.625999'
print 'dt_str   ', dt_str

# (1) parse it to build a datetime instance
dt_obj = datetime.strptime(dt_str, ISO_8601_EXTENDED)
print 'dt_obj   ', repr(dt_obj)
assert dt_str == dt_obj.strftime(ISO_8601_EXTENDED)

# (2) make an UTC time tuple, losing fractional part of seconds
dt_tuple = dt_obj.utctimetuple()
print 'dt_tuple ', repr(dt_tuple)

# (3) convert the time tuple to integer seconds from the epoch
dt_secs = calendar.timegm(dt_tuple)
print 'dt_secs  ', dt_secs

# (4) multiply seconds by 1000 to get miliseconds from the epoch
dt_milis = dt_secs * 1000
print 'dt_milis ', dt_milis

# (5) divide microseconds by 1000 and add to miliseconds
dt_milis = float(dt_obj.microsecond)/1000 + dt_milis
print 'dt_milis ', dt_milis

# (6) convert to integer
dt_milis = int(dt_milis)
print 'dt_milis ', dt_milis

# (7) check that last 4 digits of integer miliseconds 
#     also appear in the original datetime string
uni_str, mili_str = dt_str.split('.')
assert str(dt_milis).endswith(uni_str[-1]+mili_str[:3])
