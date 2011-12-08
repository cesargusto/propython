"""
    >>> from locally import Example, test_function
    >>> e = Example()
    >>> e.test_method()
    5
    >>> test_function()
    7
    >>> e = Example()
    >>> e.setValue(7)
    Traceback (most recent call last):
      ...
    AttributeError: Access denied


"""
import doctest
doctest.testmod()


