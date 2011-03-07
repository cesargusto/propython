from multiprocessing import Process
import os
from time import sleep

def info(title):
    print title
    print 'module name:', __name__
    print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f(n):
    info('f(%s)' % n)
    sleep(n)
    print 'f(%s)'  % n

if __name__ == '__main__':
    info('main line')
    delays = range(1,5)
    while delays:
        t = delays.pop() if len(delays) % 2 else delays.pop(0)
        p = Process(target=f, args=(t,))
        p.start()
        p.join()

