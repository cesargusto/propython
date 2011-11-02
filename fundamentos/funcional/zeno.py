#!/usr/bin/env python

# solução pythonica para a dicotomia de zeno

def zeno(num_termos):
    i = 1
    while i <= num_termos:
        try:
            yield float(1)/2**i
        except OverflowError:
            raise StopIteration    
        i += 1
        
for i in range(10):
    print sum(zeno(2**i))

