from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

from time import strftime

def hora_local(request):
    return Response(strftime('%H:%M:%S'))

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hora', '/')
    config.add_view(hora_local, route_name='hora')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
