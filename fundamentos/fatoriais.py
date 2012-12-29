# coding: utf-8

def fat1(n):
    for i in range(2, n):
       n *= i
    return n

def fat2(n):
    return 1 if n < 2 else n*fat2(n-1)

'''nao Pythonica: reduce não é mais built-in em Python 3 e o uso de
   lambda nao é estimulado; os principais usos de lambda tem sido
   gradualmente substituidos. ex: list compreehensions em vez de
   filter e map; sum(), any(), all() em vez de reduce etc.'''

def fat3(n):
    return reduce(lambda x,y: x*y, range(2, n+1), 1)


def testar():
    for fat in [fat1, fat2, fat3]:
        assert fat(1) == 1
        assert fat(2) == 2
        assert fat(5) == 120
        assert fat(10) == 3628800
        assert fat(21) == 51090942171709440000 # log(fat(21), 2) > 64
        assert fat(42) == 1405006117752879898543142606244511569936384000000000

if __name__=='__main__':
    testar()

