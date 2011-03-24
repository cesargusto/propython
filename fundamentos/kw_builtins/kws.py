import sys
from keyword import kwlist

ver = '_'.join(str(i) for i in sys.version_info[:3])
out = open('kw_'+ver+'.txt', 'w')
for w in kwlist:
    out.write(w+'\n')
out.close()
