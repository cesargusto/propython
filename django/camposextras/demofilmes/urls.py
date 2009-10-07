from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail

from demofilmes.models import Filme

filmes = Filme.objects.all()

urlpatterns = patterns('',
    url(r'^$', object_list, {'queryset':filmes}, name='demofilmes.indice'),
    url(r'^ver/(?P<object_id>\d+)/$', object_detail, {'queryset':filmes},
        name='demofilmes.filme'),
)

