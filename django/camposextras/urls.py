from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^demo/', include('camposextras.demofilmes.urls'), name='demofilmes'),
    url(r'^admin/', include(admin.site.urls)),
)

