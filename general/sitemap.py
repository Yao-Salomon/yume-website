from .models import Client
from django.contrib import sitemaps
from django.urls import reverse

from blog.models import Billet

class StaticViewSitemap(sitemaps.Sitemap):
    priority=0.5
    changefreq="daily"
    protocol="https"

    def items(self):
        return ['home','blog','connexion','inscription',]

    def location(self, item):
        return reverse(item)

class BlogSitemap(sitemaps.Sitemap):
    priority=0.5
    changefreq="daily"
    protocol="https"

    def items(self):
        return Billet.managed_objects.get_published_billet()
        
    def lastmod(self,obj):
        return obj.date_de_creation

class ClientSitemap(sitemaps.Sitemap):
    priority=0.5
    changefreq="daily"
    protocol="https"

    def items(self):
        return Client.objects.filter(is_referenced=True)
        
    def lastmod(self,obj):
        return obj.date_joined
