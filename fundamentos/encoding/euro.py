# -*- coding: utf-8 -*-

euro_iso = '€'
euro_unicode_a_partir_do_iso = euro_iso.decode('utf-8')
print hex(ord(euro_iso))
euro_unicode = u'€'
euro_unicode_certeza = u'\u20ac'
print hex(ord(euro_unicode))
print hex(ord(euro_unicode_certeza))
print euro_iso
print euro_unicode
print euro_unicode_certeza

