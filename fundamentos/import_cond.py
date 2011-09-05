'''
Tested with Python 2.4, 2.5, 2.6 and 3.1
'''

from sys import stdin, stdout

try:
    from hashlib import md5
except ImportError:
    from md5 import md5

entrada = stdin.read().encode('utf-8')
stdout.write(md5(entrada).hexdigest()+'\n')
