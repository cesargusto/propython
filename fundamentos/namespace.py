
'''
    >>> meta = Namespace(a = 'alfa',
    ...                  b = 'beta',
    ...                  c = 3)
    >>> n.c
    3

'''

class Namespace(object):
    def __init__(self, **kwargs):
        vars(self).update(kwargs)

if __name__=='__main__':
    import doctest
    doctest.testmod()

'''
This Namespace class comes from:

http://pypi.python.org/pypi/ast2src/2010.01.21.ast2src

For another example of a Namespace class, see:

http://www.python.org/dev/peps/pep-3104/

Also see this discussion with a comment by Alex Martelli:

http://www.velocityreviews.com/forums/t357148-can-we-create-an_object-object-and-add-attribute-like-for-a-class.html
'''
