#!/usr/bin/env python
# coding: utf-8

import sys
from xml.etree import cElementTree as ElementTree

FREEMIND_VERSION = '0.7.1'

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print 'Usage: %s <InteliMap-text-with-tabs.txt>' % sys.argv[0]
    raise SystemExit

def parse_line(line):
    parts = line.split('\t')
    level = 0
    while len(parts[level]) == 0:
        level += 1
    return (level, parts[level].strip())

map = ElementTree.Element('map', version=FREEMIND_VERSION)
map.text = '\n'
map.tail = '\n'

in_file = open(filename)
line = in_file.readline()

node = ElementTree.Element('node', TEXT=line.strip())
map.append(node)
parents = [node]
line_num = 0
for line in in_file:
    line_num += 1
    level, text = parse_line(line)
    level += 1 # correct InteliMap quirk
    level_change = level - len(parents)
    if level_change == 1:
        parents.append(node)
    elif level_change < 0:
        for i in range(abs(level_change)):
            parents.pop()
    elif level_change > 1:
        print 'Invalid text file: too many tabs indent at line', line_num
    node = ElementTree.Element('node', TEXT=text)
    node.text = '\n'
    node.tail = '\n'
    parents[-1].append(node)
    
out_name = filename.replace('.','_') + '_freemind.mm'
out_file = open(out_name, 'wb')
ElementTree.ElementTree(map).write(out_file, 'utf-8')
out_file.close()
