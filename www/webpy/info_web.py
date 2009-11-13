import os, sys
curdir = os.path.dirname(__file__)
sys.path.append(curdir)

import web
from time import strftime

urls = (
  '/(.*)', 'Info',
)

class Info:        
    def GET(self, fmt):
        saida = ['<h1>%s</h1>' % strftime('%H:%M:%S')]
        saida.append('<table>')
        for k in dir(sys):
            if k[0] == '_': continue
            html = '<tr><th>%s</th><td>%s</td></tr>'
            saida.append(html % (k, getattr(sys, k)))
        saida.append('</table>')
                
        return '\n'.join(saida)

application = web.application(urls, globals()).wsgifunc()

