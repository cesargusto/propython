from django.db import models, IntegrityError

from datetime import datetime
from random import choice

# Alphanumeric digits omitting the lowercase letter "l" to avoid confusion 
# with the digit 1. If a letter "l" occurs in user input, convert it to 1.
CLEAR_DIGITS = string.digits + string.ascii_lowercase
CLEAR_DIGITS = CLEAR_DIGITS.replace('l','')

MAX_SHORT_URL = 255
MIN_SLUG = 4
MAX_SLUG = 8 # this is the maximum length returned by gen_slug
TRIES_PER_SIZE = 3

class SlugCollision(RuntimeError):
    message = 'unable to generate unique slug'

class Url(models.Model):
    slug = models.SlugField(max_length=MAX_SLUG, unique=True, editable=False)
    url = models.TextField(max_length=4096)
    short_url = models.CharField(max_length=MAX_SHORT_URL, editable=False)
    title = models.TextField(max_length=1024, blank=True)
    write_count = models.PositiveIntegerField(default=1, editable=False)
    write_time = models.DateTimeField(default=datetime.now, editable=False)
    read_count = models.PositiveIntegerField(default=0, editable=False)
    read_time = models.DateTimeField(null=True, editable=False)
    
    def save(self):
        pos_start = self.url.find('://') + 3
        self.short_url = self.url[pos_start:MAX_SHORT_URL+pos_start]
        for tries in range(MAX_SLUG/TRIES_PER_SIZE):
            try:    
                self.slug = gen_slug(tries)
                super(Url, self).save()
            except IntegrityError, e:
                if 'column slug is not unique' in e.message:
                    continue
                else:
                    raise    
            else:
                return # success
        raise SlugCollision() # give up            

    def gen_slug(self, attempt):
        slug = ''
        while len(slug) < (MIN_SLUG+attempt/TRIES_PER_SIZE):
            slug += random.choice(CLEAR_DIGITS)
        return slug
        
    def __unicode__(self):
        return '%d%s' % (self.pk, self.url[4:120])
        
    
        

