#!/usr/bin/env python
# coding: utf-8

"""
A `CompositeString` can hold the value of an ISIS field with subfields. 
Its contents may be acessed in several ways. For example, in a Lilacs
bibliographic record, field 10 (Author) has the following subfields::

    Subcampo(s)
    ^*: autor personal
    ^1: afiliación nivel 1
    ^2: afiliación nivel 2
    ^3: afiliación nivel 3
    ^p: pais de la institución o del autor
    ^c: ciudad de la institución
    ^r: responsabilidad del autor

For example, here are two ocurrences of field 10::

    rec.v10 = [CompositeString('Renato Murasaki^1MTI^2BIREME^pBrasil^cSão Paulo^rEditor'),
               CompositeString('Eidi Abdala^1Biblioteca Central^2Faculdade de Saúde Pública' 
                               '^3Universidade de São Paulo^pBrasil^cSão Paulo^rEditor')]

Different ways to access::

    a = v10[0]  --> a is the first occurrence of the field
    unicode(a)  --> u'Renato Murasaki^1MTI^2BIREME^pBrasil^cSão Paulo^rEditor'
    a._         --> Renato Murasaki
    a.p         --> Brasil
    a.r         --> Editor
    a['p']      --> Brasil (allows indirect access)
    a['1']      --> MTI (numeric subfields must be indexed by strings)
    a(2)        --> BIREME (shortcut for numeric subfields)
    a('es')     --> the Spanish version of a multilingual record
    list(a)     --> ['Renato Murasaki','MTI','BIREME','Brasil','São Paulo', 'Editor']
    list(a)[0]  --> 'Renato Murasaki' (first subfield)
    list(a)[:3] ?-> ['Renato Murasaki','MTI','BIREME'] first 3 subfields
    iter(a)     ?-> iterator over the subfield keys (like iter(a_dict)) ?
    iter(a.value) ?-> iterator over content characters (like iter(a_string)) ?

Testing::

    >>> f = CompositeString(u'Ficciones')
    >>> f.parse()
    >>> f._parts
    {u'_': u'Ficciones'}
    >>> a = CompositeString(u'The Annotated Alice^sDefinitive Edition', subfields=u's')
    >>> a.parse()
    >>> a._parts
    {u's': u'Definitive Edition', u'_': u'The Annotated Alice'}
    >>> x = CompositeString(u'The Annotated Alice^xDefinitive Edition', subfields=u's')
    >>> x.parse(strict=True)
    Traceback (most recent call last):
      ...
    TypeError: Unexpected subfield "x"
    >>> y = CompositeString(u'The Annotated Alice^xDefinitive Edition', subfields=u's')
    >>> y.parse()
    >>> y._parts
    {u'x': u'Definitive Edition', u'_': u'The Annotated Alice'}
    >>> imprenta = CompositeString(u'^aRio de Janeiro^bEditora Acme^c1963')
    >>> imprenta.parse()
    >>> imprenta._parts
    {u'a': u'Rio de Janeiro', u'c': u'1963', u'b': u'Editora Acme', u'_': u''}
"""

class CompositeString(object):
    _value = u''
    
    def __init__(self, value=u'', subfields=u'', subfield_prefix=u'^'):
        self._value = value
        self._subfields = subfields
        self._subfield_prefix = subfield_prefix
        self._parts = {}
        
    def parse(self, strict=False):
        parts = self._value.split(self._subfield_prefix)
        if strict:
            qt_subs = len(self._subfields)+1
            if len(parts) > qt_subs:
                raise TypeError('There are more parts than declared subfields.')
        subfields = set(self._subfields)
        self._parts[u'_'] = parts.pop(0)
        for part in parts:
            prefix = part[0]
            self._parts[prefix] = part[1:]
            try:
                subfields.remove(prefix)
            except KeyError:
                if strict:
                    raise TypeError('Unexpected subfield "%s"' % prefix)            

        
if __name__=='__main__':
    import doctest
    doctest.testmod()
            
              
    
