# coding: utf-8

from pprint import pformat
from cgi import escape

from google.appengine.ext.webapp import WSGIApplication, RequestHandler
from google.appengine.ext.webapp.util import run_wsgi_app

ENVELOPE = '''
<html><head><title>%(titulo_pagina)s</title></head>
<body>
<h1>%(titulo_pagina)s</h1>
%(miolo)s
</body>
</html>
'''

class Principal(RequestHandler):
    def get(self):
        titulo_pagina = 'Aprenda a programar'
        miolo = '<a href="/req">A requisição</a>'
        self.response.out.write(ENVELOPE % locals())
        
def prep(o):
    ''' prepara objeto para saída html '''
    return escape(pformat(o))

class Requisicao(RequestHandler):
    def get(self):
        titulo_pagina = 'A requisição'
        req = self.request
        miolo = []
        miolo.append('<pre>%s</pre>' % prep(req))
        miolo.append('<pre>%s</pre>' % prep(dir(req)))
        miolo.append('<pre>')
        for atrib in (a for a in dir(req) if not any((a.startswith('_'), a.endswith('environ')))):
            miolo.append('%28s = %s' % (atrib, prep(getattr(req, atrib))))
        miolo.append('</pre>')
        miolo.append('<pre>%s</pre>' % prep(req.environ))
        miolo = '\n'.join(miolo)
        self.response.out.write(ENVELOPE % locals())

if __name__ == '__main__':
    aplicacao = WSGIApplication([   
                                ('/', Principal),
                                ('/req', Requisicao),                                     
                                ], debug=True)
    run_wsgi_app(aplicacao)

