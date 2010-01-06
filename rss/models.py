from django.db import models
class Item(models.Model):
    """Rss Item"""
    title = models.CharField(blank=True, max_length=500)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True, verify_exists=False)
    pubDate = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    
    class Meta:
        ordering = []
        verbose_name, verbose_name_plural = "", "s"

    def __unicode__(self):
        return u""

    @models.permalink
    def get_absolute_url(self):
        return ('', [self.id])
# Create your models here.
