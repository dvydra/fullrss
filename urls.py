from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^rss/import/(\d+)', 'rss.views.importFeed'),        
    (r'^rss/render/(\d+)', 'rss.views.renderFeed'),    
)
