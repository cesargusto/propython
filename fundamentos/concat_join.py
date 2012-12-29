import timeit

concat = '''
s = b''
n = 1
while n < 1000:
    s += b'x' * num_chars
    n += 1
'''

join = '''
s = []
n = 1
while n < 1000:
    s.append(b'x' * num_chars)
    n += 1
s = b''.join(s)
'''

times = 100

for num_chars in [1, 10, 100, 1000, 10000]:
    start = 'num_chars = %d' % num_chars
    print(start)
    print('join  : %0.3f' % timeit.timeit(concat, setup=start, number=times))
    print('concat: %0.3f' % timeit.timeit(join, setup=start, number=times))
    print('')

