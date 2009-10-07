from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^demo/', include('camposextras.demofilmes.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

