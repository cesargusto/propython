import sys

total = 0
for arg in sys.argv[1:]:
    try:
        total += float(arg)
    except ValueError:
        print 'ignorado: %r' % arg
    else:
        print arg
print '-' * 20
print total

