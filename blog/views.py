from pprint import pprint
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from banner.models import Banner
from rest_framework import viewsets
from general.constantes import CURRENCY_UNIT
from general.models import Utilitaire, Valeur
from .models import Billet
from .serializers import BlogSerializer
from general.permissions import IsAdmnAuthenticated
from django.urls import resolve

class PartieDetailView(DetailView):
   pass

class BlogListView(ListView):
    template_name='blog/index.html'
    context_object_name="blog"
    paginate_by=20
    next="blog"

    def get(self, request, *args, **kwargs):
        self.next=resolve(request.path).url_name
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset=Billet.managed_objects.get_published_billet()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #contexte généraux à toute les pages
        context["utilitaires"] = Utilitaire.managed_objects.get_last_utilitaire()

        context["valeurs"]= list(Valeur.objects.all())
        context["utiles"]={
            "currency":CURRENCY_UNIT,
        }
        context['next']=self.next
        context["random_banner"]=Banner.objects_random.get_random_banner()
        context["seo"]={
            'title':"Blog | Yume, Votre solution digital-création d'applications web et mobile",
            'category':"Blog, Site internet, Applications Web, Applications mobile, référencement organique",
            'description':"Le blog de yume vous apporte le meilleur du digital à Abidjan, Yamoussoukro et partout ailleurs en Côte D'Ivoire.",
            'robots':None,
            'keywords':"Blog, Blog Yume Côte D'Ivoire, Côte D'Ivoire, Yume Abidjan, Yume, Yume Yamoussoukro, Blog Application Web, Application Mobile",
            'schema':"",
        }
        context['og']={
            'title':"Blog|Yume Découvrez une nouvelle façon de penser web",
            'site-name':"Yume",
            'descritpion':"Le blog de yume vous apporte le meilleur du digital à Abidjan, Yamoussoukro et partout ailleurs en Côte D'Ivoire.",
            'url':self.request.build_absolute_uri,
            'type':"Website",
            'image':None,
        }
        
        return context
    


class BilletDetailView(DetailView):
    template_name='blog/billet.html'
    context_name='billet'
    next="home"

    def get(self, request, *args, **kwargs):
        self.next=resolve(request.path).url_name
        return super().get(request, *args, **kwargs)
    
    def get_object(self, queryset=Billet.managed_objects.get_published_billet()):
        billet=super().get_object(queryset)
        billet.purify()
        return billet
    
    def get_partie(self):
        billet=super().get_object(Billet.managed_objects.get_published_billet())
        parties=billet.partie_set.all()
        for partie in parties:
            partie.purify()
            pprint(partie)
        return parties

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #contexte généraux à toute les pages
        context["utilitaires"] = Utilitaire.managed_objects.get_last_utilitaire()
        context["valeurs"]= list(Valeur.objects.all())
        context["next"]=self.next
        context["utiles"]={
            "currency":CURRENCY_UNIT,
        }
        context["random_banner"]=Banner.objects_random.get_random_banner()
        context["seo"]={
            'title':self.get_object().titre,
            'category':"Article de Blog",
            'description':self.get_object().introduction[0:150],
            'robots':None,
            'keywords':"Yume, Blog, Création de site internet, SEO"+self.get_object().introduction[0:10],
            'schema':None,
        }
        context['og']={
            'title':self.get_object().titre,
            'site-name':"Yume",
            'descritpion':self.get_object().introduction[0:50],
            'url':self.request.build_absolute_uri,
            'type':"Website",
            'image':None,
        }
        #contextspécifique
        context['parties']= self.get_partie()

        return context
    

class BilletPreviewDetailView(DetailView):
    pass


#vue pour le frameworks djangorest

class BilletViewset(viewsets.ReadOnlyModelViewSet):
    
    serializer_class=BlogSerializer

    def get_queryset(self):

        queryset=Billet.managed_objects.get_published_billet()
        id=self.request.GET.get('id')

        if id is not None:
            queryset=queryset.filter(id=id)

        return queryset