#!/usr/bin/env python
# coding: utf-8
import sys
from xml.etree import ElementTree

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print 'Usage: %s <freemind-file.mm>' % sys.argv[0]
    raise SystemExit

def walk(e, action, level=0):
    action(e, level)
    for child in e.getchildren():
        walk(child, action, level=level+1)

def action(e, level):
    # handle top level anomaly in InteliMap
    # where level=0 and level=1 are not indented
    level = level - 1 if level else level
    indent = '\t'*level
    print '%s%s' % (indent, e.get('TEXT'))

map = ElementTree.parse(filename)
docroot = map.getroot()
root = docroot.getchildren()[0]

walk(root, action)
