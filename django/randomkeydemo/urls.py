from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # (r'^randomkeydemo/', include('randomkeydemo.foo.urls')),

    (r'^admin/', include(admin.site.urls)),
)
