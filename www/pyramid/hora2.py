from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

from time import strftime

@view_config(name='hora', request_method='GET')
def hora_local(request):
    return Response(strftime('@%H:%M:%S'))

if __name__ == '__main__':
    config = Configurator()
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
