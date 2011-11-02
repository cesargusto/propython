from string import ascii_uppercase, digits
from itertools import product

def placas(len_prefix, len_sufix):
    return (''.join(pre)+''.join(suf) for pre, suf in
                product(
                    product(*((ascii_uppercase,)*len_prefix)),
                    product(*((digits,)*len_sufix))))

for p in placas(2, 3):
    print p

