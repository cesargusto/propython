
'''
>>> l = [1, 2, 3, 4, 4, 54, 5, 23, 34, 32, 3]
>>> l
[1, 2, 3, 4, 4, 54, 5, 23, 34, 32, 3]
>>> d = {}
>>> [d.__setitem__(x, 0) for x in l] #doctest:+ELLIPSIS
[...]
>>> [d.__setitem__(x, d.__getitem__(x) + 1) for x in l]  #doctest:+ELLIPSIS
[...]
>>> d
{32: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 1, 34: 1, 54: 1, 23: 1}
'''
    