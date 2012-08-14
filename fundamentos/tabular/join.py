#!/usr/bin/env python

import pickle
from operator import attrgetter

from join_hdi import Statistics

with open('hdi-stats.pickle') as dump:
    hdi_stats = pickle.load(dump)

class Country(object):
    __slots__ = ('name', 'gold', 'silver', 'bronze',
                 'population', 'gdp', 'hdi', 'life', 'school')
    def __init__(self, name, gold, silver, bronze):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    @property
    def medals(self):
        return self.gold + self.silver + self.bronze

    @property
    def medals_per_mil(self):
        return self.medals/self.population


countries = {}

with open('medals-2012.txt') as medals:
    for lin in medals:
        _, name, gold, silver, bronze, total = lin.split('\t')
        name = name.strip()
        countries[name] = Country(name, int(gold), int(silver), int(bronze))

name_map = { # medal table -> HDI table
    'Great Britain': 'United Kingdom',
    'Hong Kong, China': 'Hong Kong, China (SAR)',
    'Islamic Republic of Iran': 'Iran (Islamic Republic of)',
    "People's Republic of China": 'China',
    'Republic of Korea': 'Korea (Republic of)',
    'Republic of Moldova': 'Moldova (Republic of)',
    'United States of America': 'United States',
    'Venezuela': 'Venezuela (Bolivarian Republic of)',
}

no_stats = {
    'Cuba',
    "Democratic People's Republic of Korea",
    'Grenada',
    'Puerto Rico',
    'Taipei (Chinese Taipei)',
}

for country in sorted(countries.values(), key=attrgetter('medals'), reverse=True):
    if country.name in hdi_stats:
        key = country.name
    else:
        key = name_map.get(country.name)
        if key is None:
            assert country.name in no_stats
            continue
    print country.name
    for atrib in Country.__slots__:
        if hasattr(hdi_stats[key], atrib):
            value = getattr(hdi_stats[key], atrib)
            setattr(country, atrib, value)
COLUMNS = 12
def table_html():
    html = ['<table id="main-table" class="tablesorter">',
            '<thead>',
            '<tr>',
            ]
    for atrib in Country.__slots__:
        html.append('\t<th>'+atrib+'</th>')
        if atrib == 'bronze':
            html.append('\t<th>medals</th>')
        if atrib == 'population':
            html.append('\t<th>medals/million</th>')
        if atrib == 'gdp':
            html.append('\t<th>gdp/c</th>')
    html.append('</tr>')
    html.append('</thead>')
    html.append('<tbody>')

    for country in sorted(countries.values(), key=attrgetter('gold'), reverse=True):
        html.append('<tr>')
        column_count = 0
        for atrib in Country.__slots__:
            try:
                column_count += 1
                value = getattr(country, atrib)
                class_ = ''
                if atrib == 'name':
                    class_ = ' class="name"'
                elif atrib == 'gold':
                    value = '<img src="yellow.gif" width="{0}" height="14" align="left">{0}'.format(value)
                elif atrib == 'bronze':
                    value = '{}</td><td>{}</td>'.format(value, country.medals)
                    column_count += 1
                elif atrib == 'population':
                    value = '{:.3f}</td><td>{:.3f}</td>'.format(value, country.medals/value)
                    column_count += 1
                elif atrib == 'gdp':
                    value = '{:.0f}</td><td>{:.0f}</td>'.format(value, value/country.population*1000)
                    column_count += 1
                elif atrib == 'hdi':
                    value = format(value, '0<5.3')
            except AttributeError:
                value = '*'
                html.append('\t<td class="no-data" colspan="%s"><a href="#sources">(no HDR data)</a></td>' % (COLUMNS-(column_count-1)))
                break
            html.append('\t<td%s>%s</td>' % (class_, value))

        html.append('</tr>')

    html.append('</tbody>')
    html.append('</table>')
    return '\n'.join(html)+'\n'

INSERT_MARK = '<!--main-table-->'
with open('html/template.html') as template, open('html/index.html','w') as outfile:
    html = template.read()
    assert INSERT_MARK in html
    table = table_html()
    print table
    html = html.replace(INSERT_MARK, INSERT_MARK+'\n'+table)
    outfile.write(html)


