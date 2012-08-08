from operator import attrgetter

class Country(object):
    def __init__(self, name, pop):
        self.name = name
        self.pop = pop

    @property    
    def medals_per_mil(self):
        return self.medals/self.pop
        
        
table = open('hdr-pop.txt')

countries = {}

for lin in table:
    _, name, pop = lin.split('\t')
    name = name.strip()
    pop = pop.replace(',', '')
    countries[name] = Country(name, float(pop))
    
table.close()

medals = open('medals-2008.txt')

name_map = {
    'Great Britain & N. Ireland': 'United Kingdom',
    'Iran': 'Iran (Islamic Republic of)',
    'Moldova': 'Moldova (Republic of)',
    'Russia': 'Russian Federation',
    'South Korea': 'Korea (Republic of)',
    'Venezuela': 'Venezuela (Bolivarian Republic of)',
    'Vietnam': 'Viet Nam',
}

# 'Chinese Taipei', 'Cuba', 'North Korea'


not_found = []
for lin in medals:
    _, name, gold, silver, bronze, total = lin.split('\t')
    name = name.strip()
    if name not in countries:
        try:
            name = name_map[name]
        except KeyError:
            continue
    country = countries[name]
    country.medals = int(total)

country_list = [c for c in countries.values() if hasattr(c, 'medals')]
for country in sorted(country_list, key=attrgetter('medals_per_mil'), reverse=True):
    print country.medals, country.pop, float(country.medals_per_mil), country.name
    
    
    
    

