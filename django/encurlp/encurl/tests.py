from django.test import TestCase
from django.db import IntegrityError

from models import Url, MIN_SLUG, MAX_SLUG, SlugCollision

MOCK_MARK = 'MoCk'*3

def mock_hash_slug(self):
    ''' used to monkey-patch the Url class for SlugGeneration tests '''
    if MOCK_MARK in self.url:
        return (MOCK_MARK*3)[:MAX_SLUG]
    else:
        raise TypeError('mock_hash_slug invoked on non-mock Url instance')

class SlugGeneration(TestCase):

    def setUp(self):
        # monkey patch class to generate testable slugs
        self.real_hash_slug = Url.hash_slug
        Url.hash_slug = mock_hash_slug

    def test_mock_generation(self):
        """
        Tests that a mock slug is properly generated
        """
        u1 = Url(url='http://lab.tmp.br/%s/index.html' % MOCK_MARK)
        u1.save()
        self.assertEqual(u1.slug, MOCK_MARK[:MIN_SLUG])

    def test_slug_shortening(self):
        """
        Tests that a slug is properly generated
        """
        u1 = Url(url='http://lab.tmp.br/%s/index.html' % MOCK_MARK)
        u1.save()
        u2 = Url(url='http://another.lab.tmp.br/%s/index.html' % MOCK_MARK)
        u2.save()
        u3 = Url(url='http://yetanother.lab.tmp.br/%s/index.html' % MOCK_MARK)
        u3.save()
        self.assertEqual(u1.slug, MOCK_MARK[:MIN_SLUG])
        self.assertEqual(u2.slug, MOCK_MARK[:MIN_SLUG+1])

    def test_slug_shortening_failure(self):
        """
        When a slug cannot be generated, SlugCollision is raised
        """
        u = Url(url='http://lab.tmp.br/%s/index.html' % MOCK_MARK)
        u.save()
        slug = u.slug
        while len(slug) < MAX_SLUG:
            uu = Url(url='http://another.lab.tmp.br/%s/index%s.html' % (MOCK_MARK, len(slug)))
            uu.save()
            slug = uu.slug
        uuu = Url(url='http://last.lab.tmp.br/%s/index%s.html' % (MOCK_MARK, len(slug)))
        self.assertRaises(SlugCollision, uuu.save)

    def tearDown(self):
        Url.hash_slug = self.real_hash_slug


__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

