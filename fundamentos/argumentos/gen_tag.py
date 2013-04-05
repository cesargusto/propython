'''
	>>> tag('br')
	'<br />'

    >>> tag('img', src='bla')
    '<img src="bla" />'

    >>> gera_atribs({'b':2, 'a':1})
    'a="1" b="2"'

    >>> gera_atribs({})
    ''

    >>> tag("link", rel='xxx', bla='bagulho')
    '<link bla="bagulho" rel="xxx" />'



'''

def gera_atribs(d):
    s = ''
    for c, v in sorted(d.items()):
        s += '%s="%s" ' % (c, v)

    return s.rstrip()

def tag(nome, **kwargs):
    '''gera tags HTML'''
    if kwargs:
        return '<%s %s />' % (nome, gera_atribs(kwargs))
        #return '<%s src="%s" />' % (nome, src)
    else:
        return '<%s />' % nome
