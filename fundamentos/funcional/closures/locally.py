"""
from: http://www.builderau.com.au/blogs/byteclub/viewblogpost.htm?p=339270875
user "sth" wrote:

You can wrap the value in a function closure. This way the value itself doesn't show up in dict(), just the function that produces the value.

That said, I wouldn't recommend anyone to actually use this. For normal class interface purposes it should be absolutely enough to make clear to the user which variables are "private", like by prefixing their names with "_". So everybody who wants to use/change them knows this is dangerous/unsafe/unsupported.

LR: updated exceptions from plain strings to AttributeError, and added doctest here::

    >>> e = Example()
    >>> e.test_method()
    5
    >>> test_function()
    7
    >>> e.getValue()
    Traceback (most recent call last):
      ...
    AttributeError: Access denied
"""
import inspect

def islocalcall():
    stack = inspect.stack()
    #log = open('log','a')
    #log.write('stack[1][1] = %s; stack[2][1] = %s\ns' % (stack[1][1], stack[2][1]))
    #log.flush()
    #log.close()
    try:
        # check for same file
        # note that doctests run from a <doctest __main__[n]> pseudo-file
        return (stack[1][1] == stack[2][1])
    finally:
        del(stack)

class Example(object):
    def __init__(self):
        self.setValue(None)

    def setValue(self, v):
        if not islocalcall():
            raise AttributeError("Access denied")
        def restrictedValue():
            if not islocalcall():
                raise AttributeError("Access denied")
            return v
        self.getValue = restrictedValue

    def test_method(self):
        self.setValue(5)
        print self.getValue()

def test_function():
    e = Example()
    e.setValue(7)
    print e.getValue()
        
if __name__=='__main__':
    import doctest
    doctest.testmod()


