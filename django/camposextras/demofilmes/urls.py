# coding: utf-8

from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object

from demofilmes.models import Filme
from demofilmes.views import cadastrar

filmes = Filme.objects.all()

def url_indice():
    return reverse('demofilmes.indice')

urlpatterns = patterns('',
    # CRUD básico com generic views
    url(r'^$', object_list, 
        {'queryset':filmes}, 
        name='demofilmes.indice'),
    url(r'^ver/(?P<object_id>\d+)/$', object_detail, 
        {'queryset':filmes},
        name='demofilmes.ver'),
    url(r'^simples/$', create_object, 
        {'model':Filme}, 
        name='demofilmes.simples'),
    url(r'^edtit/(?P<object_id>\d+)/$', update_object, 
        {'model':Filme}, 
        name='demofilmes.edtit'),
    # TODO: como retirar esta URL hardcoded? reverse aqui não funciona...
    url(r'^del/(?P<object_id>\d+)/$', delete_object, 
        {'model':Filme, 'post_delete_redirect':'/demo/'}, 
        name='demofilmes.del'),
    # insert e update com múltiplos objetos relacionado
    url(r'^cadastrar/$', cadastrar, 
        name='demofilmes.cadastrar'),
    url(r'^editar/(?P<filme_id>\d+)/$', cadastrar, 
        name='demofilmes.editar'),
)

