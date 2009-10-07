from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.core.urlresolvers import reverse

from demofilmes.models import Filme

filmes = Filme.objects.all()

urlpatterns = patterns('',
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
    url(r'^del/(?P<object_id>\d+)/$', delete_object, 
        {'model':Filme, 'post_delete_redirect':'/demo/'}, 
        name='demofilmes.del'),
)

