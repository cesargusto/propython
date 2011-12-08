from timeit import timeit

prep = """
x = 1.1
t = 0
"""
soma = """
for i in range(10**6):
    t += x
print t
"""
print timeit(soma, prep, number=1)
prep = """
from decimal import Decimal
x = Decimal('1.1')
t = Decimal(0)
"""
print timeit(soma, prep, number=1)
prep = """
from decimal import Decimal, getcontext
getcontext().prec = 10
x = Decimal('1.1')
t = Decimal(0)
"""
print timeit(soma, prep, number=1)


