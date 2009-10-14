from django.db import models, IntegrityError

from base64 import urlsafe_b64encode, urlsafe_b64decode
from hashlib import sha1
from datetime import datetime

class SlugCollision(RuntimeError):
    message = 'unable to generate unique slug'

MIN_SLUG = 4
MAX_SLUG = 27 # this is the maximum length returned by hash_slug

class Url(models.Model):
    slug = models.SlugField(max_length=MAX_SLUG, unique=True, editable=False)
    url = models.TextField(max_length=4096)
    title = models.TextField(max_length=1024, blank=True)
    write_count = models.PositiveIntegerField(default=1, editable=False)
    write_time = models.DateTimeField(default=datetime.now, editable=False)
    read_count = models.PositiveIntegerField(default=0, editable=False)
    read_time = models.DateTimeField(null=True, editable=False)
    
    def save(self):
        temp = self.hash_slug()
        try:    
            self.slug = temp[:MIN_SLUG]
            super(Url, self).save()
        except IntegrityError, e:
            # increase length of slug until it is unique
            if 'column slug is not unique' in e.message:
                for i in range(MIN_SLUG+1, MAX_SLUG+1):
                    try:
                        self.slug = temp[:i]
                        super(Url, self).save()
                    except IntegrityError, e:
                        if 'column slug is not unique' in e.message:
                            pass
                    else:
                        return # success
            raise SlugCollision() # give up            

    def hash_slug(self):
        sh = sha1()
        sh.update(self.url)
        return urlsafe_b64encode(sh.digest())[:-1] # remove trailing =

    def __unicode__(self):
        return '%d%s' % (self.pk, self.url[4:120])
        
    
        

