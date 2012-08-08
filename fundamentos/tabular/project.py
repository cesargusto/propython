import csv
import itertools

#table = csv.reader(open('HDR-demography.csv'))
#table = csv.reader(open('HDR-economy.csv'))
table = csv.reader(open('HDR-hdi.csv'))

for lin in table:
    try:
        rank = int(lin[0])
    except ValueError:
        continue
    # HDR-demography.csv HDI rank, name, population  
    #print '\t'.join([lin[0], lin[1], lin[4]])
    # HDR-economy.csv HDI rank, name, GDP, GDP/capita  
    # print '\t'.join([lin[0], lin[1], lin[2], lin[6]])
    # HDR-hdi.csv HDI rank, name, HDI, life exp, yrs schooling  
    print '\t'.join([lin[0], lin[1], lin[2], lin[4], lin[6]])
