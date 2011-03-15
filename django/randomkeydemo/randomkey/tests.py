'''

    >>> from models import Reserva
    >>> r = Reserva(nome='Fulano', data_viagem='2009-10-23')
    >>> r.save()
    >>> 
'''
from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

