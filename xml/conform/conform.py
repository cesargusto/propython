# coding: utf-8

from xml.etree import ElementTree
from os.path import split

edl = ElementTree.parse('testeEDL_XML.xml')

raiz = edl.getroot()

#videos = [e.text for e in raiz.findall('sequence/media/video/track/clipitem/file/pathurl')]

for video in raiz.findall('sequence/media/video/track/clipitem/file/pathurl'):
    print split(video.text)[1]


