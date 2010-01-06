from django.contrib import admin
from fullrss.rss.models import Feed,Item

admin.site.register(Feed)
admin.site.register(Item)