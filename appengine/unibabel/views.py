# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response

import datetime

from utils import columnize, rowize, block_firsts, blocks, UnicodeChar

# source for charmaps: http://docs.python.org/_sources/library/codecs.txt
legacy_urls = (
    ('latin_1',     u'Western Europe', 
     'iso-8859-1, iso8859-1, 8859, cp819, latin, latin1, L1'),
    ('cp1140',      u'Western Europe', 'ibm1140'),
    ('cp1252',      u'Western Europe', 'windows-1252'),
    ('cp500',       u'Western Europe', 'EBCDIC-CP-BE, EBCDIC-CP-CH, IBM500'),
    ('cp850',       u'Western Europe', '850, IBM850'),
    ('iso8859_15',  u'Western Europe', 'iso-8859-15'),
    ('mac_roman',   u'Western Europe', 'macroman'),
    ('cp1256',      u'Arabic', 'windows1256'),
    ('cp864',       u'Arabic', 'IBM864'),
    ('iso8859_6',   u'Arabic', 'iso-8859-6, arabic'),
    ('cp1257',      u'Baltic languages', 'windows-1257'),
    ('cp775',       u'Baltic languages', 'IBM775'),
    ('iso8859_13',  u'Baltic languages', 'iso-8859-13'),
    ('iso8859_4',   u'Baltic languages', 'iso-8859-4, latin4, L4'),
    ('cp1251',      u'Bulgarian, Byelorussian, Macedonian, Russian, Serbian', 
     'windows-1251'),
    ('cp855',       u'Bulgarian, Byelorussian, Macedonian, Russian, Serbian', 
     '855, IBM855'),
    ('iso8859_5',   u'Bulgarian, Byelorussian, Macedonian, Russian, Serbian', 
     'iso-8859-5, cyrillic'),
    ('mac_cyrillic',u'Bulgarian, Byelorussian, Macedonian, Russian, Serbian', 
     'maccyrillic'),
    ('cp863',       u'Canadian', '863, IBM863'),
    ('iso8859_14',  u'Celtic languages', 'iso-8859-14, latin8, L8'),
    ('cp1250',      u'Central and Eastern Europe', 'windows-1250'),
    ('cp852',       u'Central and Eastern Europe', '852, IBM852'),
    ('iso8859_2',   u'Central and Eastern Europe', 'iso-8859-2, latin2, L2'),
    ('mac_latin2',  u'Central and Eastern Europe', 
     'maclatin2, maccentraleurope'),
    ('cp865',       u'Danish, Norwegian', '865, IBM865'),
    ('ascii',       u'English', '646, us-ascii'),
    ('cp037',       u'English', 'IBM037, IBM039'),
    ('cp437',       u'English', '437, IBM437'),
    ('iso8859_3',   u'Esperanto, Maltese', 'iso-8859-3, latin3, L3'),
    ('cp1253',      u'Greek', 'windows-1253'),
    ('cp737',       u'Greek', ''),
    ('cp869',       u'Greek', '869, CP-GR, IBM869'),
    ('cp875',       u'Greek', ''),
    ('iso8859_7',   u'Greek', 'iso-8859-7, greek, greek8'),
    ('mac_greek',   u'Greek', 'macgreek'),
    ('cp1255',      u'Hebrew', 'windows-1255'),
    ('cp424',       u'Hebrew', 'EBCDIC-CP-HE, IBM424'),
    ('cp856',       u'Hebrew', ''),
    ('cp862',       u'Hebrew', '862, IBM862'),
    ('iso8859_8',   u'Hebrew', 'iso-8859-8, hebrew'),
    ('cp861',       u'Icelandic', '861, CP-IS, IBM861'),
    ('mac_iceland', u'Icelandic', 'maciceland'),
    ('iso8859_10',  u'Nordic languages', 'iso-8859-10, latin6, L6'),
    ('cp860',       u'Portuguese', '860, IBM860'),
    ('cp866',       u'Russian', '866, IBM866'),
    ('koi8_r',      u'Russian', ''),
    ('cp874',       u'Thai', ''),
    ('cp1026',      u'Turkish', 'ibm1026'),
    ('cp1254',      u'Turkish', 'windows-1254'),
    ('cp857',       u'Turkish', '857, IBM857'),
    ('iso8859_9',   u'Turkish', 'iso-8859-9, latin5, L5'),
    ('mac_turkish', u'Turkish', 'macturkish'),
    ('koi8_u',      u'Ukrainian', ''),
    ('cp1006',      u'Urdu', ''),
    ('cp1258',      u'Vietnamese', 'windows-1258'),
)    


def main(request):
    title = u'Unibabel V.1'
    block_pages = [dict(title=title, url='/block/%x'%first) for first, l, title in blocks]
    legacy_pages = [dict(title=title, url='/legacy/%s/'%encoding, aliases=aliases) 
                    for encoding, title, aliases in legacy_urls]
    return render_to_response('mainpage.django.html', locals())

COLS = 32

def block_page(request, first):
    first = int(first, 16)
    last, title = block_firsts[first]
    columns = rowize([UnicodeChar(i) for i in xrange(first, last+1)], COLS)
    col_heads = ['%x'%(i%0x10) for i in range(COLS)]
    return render_to_response('chartable.django.html', locals())

def legacy_page(request, encoding, title, aliases):
    first, last = (0x00, 0xFF)
    chars = []
    for i in xrange(0xFF):
        try:
            char = ord(chr(i).decode(encoding))
        except UnicodeDecodeError:
            char = 0
        chars.append(char)    
    
    columns = rowize([UnicodeChar(i) for i in chars], COLS)
    col_heads = ['%x'%(i%0x10) for i in range(COLS)]
    return render_to_response('chartable.django.html', locals())
    
def char_detail(request, codepoint):
    char = UnicodeChar(int(codepoint, 16))
    return render_to_response('chardetail.django.html', locals())
    
