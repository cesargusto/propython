#!/usr/bin/env python
# coding: utf-8

from xml.etree import ElementTree

map = ElementTree.parse('crtp-freemind.mm')

docroot = map.getroot()

root = docroot.getchildren()[0]

def walk(e, level=0):
    indent = '  '*level
    print '%s%s: %s' % (indent, e.tag, e.get('TEXT'))
    for child in e.getchildren():
        walk(child, level+1)

walk(root)



