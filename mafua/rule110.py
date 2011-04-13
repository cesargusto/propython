
from random import choice

WIDTH = 120

# current pattern            111 110 101 100 011 010 001 000
# new state for center cell   0   1   1   0   1   1   1   0

rule = {'111':' ',
        '11 ':'1',
        '1 1':'1',
        '1  ':' ',
        ' 11':'1',
        ' 1 ':'1',
        '  1':'1',
        '   ':' ',
       }


curr_gen = ''.join([choice([' ','1']) for i in range(WIDTH)])
while True:
    first = rule[curr_gen[-1] + curr_gen[:2]]
    last =  rule[curr_gen[-2:] + curr_gen[0]]
    rest = ''
    for i in range(0,len(curr_gen)-2):
        rest += rule[curr_gen[i:i+3]]
    curr_gen = first + rest + last    
    print curr_gen
