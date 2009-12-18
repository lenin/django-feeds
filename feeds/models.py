from django.db import models

class FeedManager(models.Manager):
    def get_query_set(self):
        return super(FeedManager, self).get_query_set().filter(is_active=True)

class Feed(models.Model):
    name = models.CharField('nombre', max_length=100, blank=True)
    url = models.CharField(max_length=100)
    is_active = models.BooleanField(u'activo', default=True)

    objects = models.Manager()
    active = FeedManager()

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.url)

