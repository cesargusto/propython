# coding: utf-8

def application(environ, start_response):
    status = '200 OK'
    output = '<h1>Olá, WSGI!</h1>'

    response_headers = [('Content-type', 'text/html;charset=utf-8'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
