#!/usr/bin/env python

import pickle

class Statistics(object):
    def __init__(self, country_name, population):
        self.country_name = country_name
        self.population = population

stats = {}

with open('hdr-pop.txt') as table:
    for lin in table:
        _, name, pop = lin.split('\t')
        name = name.strip()
        pop = float(pop.replace(',', ''))

        stats[name] = Statistics(name, pop)

with open('hdr-gdp-gdpc.txt') as table:
    for lin in table:
        _, name, gdp, gdpc = lin.split('\t')
        if gdp == '..':
            continue
        name = name.strip()
        stats[name].gdp = float(gdp.replace(',', ''))
        stats[name].gdpc = float(gdpc.replace(',', ''))

with open('hdr-hdi-life-school.txt') as table:
    for lin in table:
        _, name, hdi, life, school = lin.split('\t')
        name = name.strip()
        stats[name].hdi = float(hdi.replace(',', ''))
        stats[name].life = float(life.replace(',', ''))
        stats[name].school = float(school.replace(',', ''))

with open('hdi-stats.pickle', 'wb') as dump_file:
    pickle.dump(stats, dump_file)


