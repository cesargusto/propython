#!/usr/bin/env python

a = 10
b = 20

def func_a():
    print a #
    return 'result of func_a'

def func_b():
    print b # referencing 'b' here causes UnboundLocalError
    assert False, 'this line is never executed'
    b = 22
    return 'result of func_b'

def func_c():
    print c # referencing 'b' here may cause UnboundLocalError
    if False:
        c = 33 # this line is unreachable, but c is seen on the left side of an assignment
    return 'result of func_c'

def test_a():
    res_a = ''
    res_a = func_a()
    assert res_a == 'result of func_a'

def test_b():
    res_b = ''
    try:
        res_b = func_b()
    except UnboundLocalError as e:
        assert e.args[0] == "local variable 'b' referenced before assignment"
    else:
        assert False, 'an UnboundLocalError excepion was expected but not raised'
    assert res_b == ''

def test_c():
    res_c = ''
    try:
        res_c = func_b()
    except UnboundLocalError as e:
        assert e.args[0] == "local variable 'b' referenced before assignment"

if __name__=='__main__':
    test_a()
    test_b()
    test_c()
    '''
    import dis
    dis.dis(func_a.__code__.co_code)
    print '*' * 70
    dis.dis(func_b.__code__.co_code)
    '''

        