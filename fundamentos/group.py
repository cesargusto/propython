from operator import itemgetter


def group(iterable, key):
    ''' groups a list of tuples according to a key

        >>> cities = [('BR','Rio de Janeiro'), ('PT', 'Porto'),
        ...     ('BR', 'Porto Alegre'),  ('PT', 'Lisboa'), ('MZ', 'Maputo')]
        >>> countries = group(cities, 0)
        >>> for country, cities in countries:
        ...     print country
        ...     for city in cities:
        ...         print '-', city[0]
        BR
        - Porto Alegre
        - Rio de Janeiro
        MZ
        - Maputo
        PT
        - Lisboa
        - Porto
        >>> countries[0]
        ('BR', [['Porto Alegre'], ['Rio de Janeiro']])
    '''
    result = []
    kvalue0 = None
    part = None
    for item in [list(i) for i in sorted(iterable, key=itemgetter(key))]:
        kvalue = item[key]
        del item[key]
        if kvalue != kvalue0:
            if part is not None:
                part[-1].sort()
                result.append(tuple(part))
            part = [kvalue, []]
            kvalue0 = kvalue
        part[-1].append(item)
    if part is not None:
        part[-1].sort()
        result.append(tuple(part))
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
