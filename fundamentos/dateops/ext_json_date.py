#!/usr/bin/env python
"""
Convert an ISO-8601 date string to the milliseconds from the epoch
integer required by the Extended JSON format used by MongoDB [1]

[1] http://www.mongodb.org/display/DOCS/Mongo+Extended+JSON

Usage::

    >>> datestr2millis('2008-04-01T03:28:50.625999')
    1207020530625
    >>> datestr2millis('1970-01-01T00:00:01.000')
    1000
    >>> datestr2millis('1970-01-01T00:00:12.345')
    12345
    >>> datestr2millis('1970-01-01T00:00:59.999')
    59999
    >>> datestr2millis('1970-01-01T00:01:00.000')
    60000
    >>> datestr2millis('9999-12-31T23:59:59.9999')
    253402300799999

"""

from datetime import datetime, timedelta

# ISO-8601 format extended to include fractions of seconds
# as seen in OpenLibrary JSON dumps
ISO_8601 = '%Y-%m-%dT%H:%M:%S.%f'

# use of timedelta.total_seconds suggested by Allison Vollmann
if hasattr(timedelta, 'total_seconds'): # for Python >= 2.7
    def datestr2millis(dt_str):
        td = datetime.strptime(dt_str, ISO_8601) - datetime(1970, 1, 1)
        return int(td.total_seconds() * 1000)
else: # for Python 2.6
    def datestr2millis(dt_str):
        td = datetime.strptime(dt_str, ISO_8601) - datetime(1970, 1, 1)
        return int((td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 1000)

if __name__=='__main__':
    import doctest
    doctest.testmod()
