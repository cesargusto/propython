import sys

total = 0
while True:
    lin = sys.stdin.readline().strip()
    if len(lin) == 0:
        break
    try:    
        total += float(lin)
    except ValueError:
        print 'ignorado: %r' % lin
print '-' * 20
print total

