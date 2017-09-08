from django.contrib import sitemaps
from django.urls import reverse

class StaticView`Sitemap(sitemaps.Sitemap):
    
    def items(self):
        return ['index', 'services', 'get_started', 'contact']

    def location(self, item):
        return reverse(item)
