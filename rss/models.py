from django.db import models
class Item(models.Model):
    """Rss Item"""
    feed = models.ForeignKey('Feed')
    title = models.CharField(blank=True, max_length=500)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True, verify_exists=False)
    guid = models.CharField(blank=True, max_length=500)
    pubDate = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    
    class Meta:
        ordering = []
        verbose_name, verbose_name_plural = "Item", "Items"

    def __unicode__(self):
        return u"Item"

    @models.permalink
    def get_absolute_url(self):
        return ('', [self.id])

class Feed(models.Model):
    """Rss Feed"""
    
    title = models.CharField(blank=True, max_length=500)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True, verify_exists=False)
    lastBuildDate = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    url = models.URLField(blank=True, verify_exists=False)
    body_element = models.CharField(blank=True, max_length=500)
    body_class = models.CharField(blank=True, max_length=500)

    class Meta:
        ordering = []
        verbose_name, verbose_name_plural = "Feed", "Feeds"

    def __unicode__(self):
        return u"Feed"

    @models.permalink
    def get_absolute_url(self):
        return ('', [self.id])
