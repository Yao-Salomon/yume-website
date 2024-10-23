"""
yume url configuration
v0.0.1

"""
from email.mime import base
from django.conf import settings
from django.contrib import admin
from django.urls import path,include, re_path
from django.conf.urls.static import static
from django.views.static import serve
from commentaires import views as commentairesviews
from django.contrib.sitemaps.views import sitemap
from general.sitemap import BlogSitemap, ClientSitemap, StaticViewSitemap
from rest_framework import routers
from agence import views as agenceviews
from blog import views as blogviews

sitemaps={

    'static':StaticViewSitemap,
    'blog':BlogSitemap,
    'client':ClientSitemap,

}

#enregistrement des routes pour l'api rest framework

router=routers.DefaultRouter()
router.register(r'produits',agenceviews.ProduitViewSet,basename='produitsjson')
router.register(r'fonctionalites',agenceviews.FonctionaliteViewSet,basename="fonctionalitejson")
router.register(r'blog',blogviews.BilletViewset,basename="blogjson")
router.register(r'commentairesblog',commentairesviews.CommentaireBlogViewset,basename="commentairesblogjson")
router.register(r'reponsesblog',commentairesviews.ReponseCommentaireBlogViewset,basename="reponsesblogjson")
urlpatterns = [
    
    path('',include('search.urls')),
    path('yumeadministration/', admin.site.urls),
    path('qui-sommes-nous/',include('about.urls')),
    path('comptes/',include('general.urls')),
    path('agence/',include('agence.urls')),
    path('blog/',include('blog.urls')),
    path('newsletter/',include('newsletter.urls')),
    path('news/',include('news.urls')),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps},name="django.contrib.sitemaps.views.sitemap"),
    path("formulaires/",include('formulaire.urls')),
    path("yume-api-auth/",include('rest_framework.urls')),
    path("yume-api/",include(router.urls)),
    path("dictionnaire/",include("dictionnaire.urls")),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns+=[
        re_path(r'^media/(?P<path>.*)$',serve,{
            'document_root':settings.MEDIA_ROOT,
        })
    ]