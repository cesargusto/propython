import string

# This is intended to be a series of alphanumeric digits that omit
# lowercase letter "l" to avoid confusion with the digit 1.
# Ocurrences of the letter "l" in user input can be converted to 1.
CLEAR_DIGITS = string.digits + string.ascii_lowercase
CLEAR_DIGITS = CLEAR_DIGITS.replace('l','')

def anybaseconv(number,fromdigits=string.digits,todigits=CLEAR_DIGITS):
    # make an integer out of the number
    x=0
    for digit in str(number):
       x = x*len(fromdigits) + fromdigits.index(digit)    
    # create the result in base 'len(todigits)'
    if x == 0:
        res = todigits[0]
    else:
        res=''
        while x>0:
            digit = x % len(todigits)
            res = todigits[digit] + res
            x = int(x / len(todigits))
    return res

def baseconv(number,todigits=CLEAR_DIGITS):
    x=int(number)
    if x == 0:
        return todigits[0]
    res=''
    while x > 0:
        digit = x % len(todigits)
        res = todigits[digit] + res
        x = int(x / len(todigits))
    return res

def split_join_left(s, sep='-', siz=4):
    res = []
    while s:
        res.append(s[:siz])
        s = s[siz:]
    return sep.join(res)    

def split_join(s, sep='.', siz=3):
    res = []
    while s:
        res.insert(0, s[-siz:])
        s = s[:-siz]
    return sep.join(res)    


def show_sample():
    import sys
    import random
    max = 17
    for i in range(0,17,2):
        n = len(CLEAR_DIGITS)**i
        for j in range(-1,2):
            ns = split_join(str(n+j))
            print '%35s %s' % (ns, split_join_left(baseconv(n+j), '-'))
    for i in range(1,16):
        b = ''
        while len(b) < i:
            b += random.choice(CLEAR_DIGITS)
        n = int(anybaseconv(b, CLEAR_DIGITS, string.digits))
        ns = split_join(str(n))
        b = split_join_left(b, '-')
        print '%35s %s' % (ns, b)
            
if __name__=='__main__':
    show_sample()
