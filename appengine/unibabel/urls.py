from django.conf.urls.defaults import patterns

from views import main, block_page, legacy_page, legacy_urls, char_detail

urls = [
    (r'^block/(.*)/', block_page),
    (r'^char/(.*)/', char_detail),
]

urls.extend( [(r'^legacy/%s/'%encoding, legacy_page, 
               {'title':title,'encoding':encoding, 'aliases':aliases}) 
              for encoding, title, aliases in legacy_urls ] )


urls.append( (r'^', main) )

urlpatterns = patterns('', *urls)
