# coding: utf-8

from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object

from demofilmes.models import Filme
from demofilmes.views import cadastrar, remover

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
    # a view genérica delete_object foi usada na view remover, e não 
    # diretamente aqui porque não descobri como passar o argumento
    # post_delete_redirect sem colocar o caminho fixo no código
    url(r'^rem/(?P<object_id>\d+)/$', remover,
        name='demofilmes.remover'),
    # insert e update com múltiplos objetos relacionado
    url(r'^cadastrar/$', cadastrar, 
        name='demofilmes.cadastrar'),
    url(r'^editar/(?P<filme_id>\d+)/$', cadastrar, 
        name='demofilmes.editar'),
)

