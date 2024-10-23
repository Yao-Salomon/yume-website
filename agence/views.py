from math import ceil
from django.views.generic import ListView
from django.shortcuts import render
from rest_framework import viewsets
from general.models import Client, Utilitaire, Valeur
from general.permissions import IsAdmnAuthenticated
from .serializers import ProduitSerializer, FonctionaliteSerializer
from .models import Produit,Fonctionalite
from general.constantes import CURRENCY_UNIT
from banner.models import Banner
from django.urls import resolve

class ClientListView(ListView):
    queryset=Client.objects.filter(is_referenced=True).order_by('stars')
    template_name='agence/annuaire.html'
    context_object_name="clients"
    paginate_by=20

    next="home"

    def get(self, request, *args, **kwargs):
        self.next=resolve(request.path).url_name
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #contexte généraux à toute les pages
        context['next']=self.next
        context["valeurs"]= list(Valeur.objects.all())
        context["utilitaires"] = Utilitaire.managed_objects.get_last_utilitaire()
        context["valeurs"]= list(Valeur.objects.all())
        context["utiles"]={
            "currency":CURRENCY_UNIT,
        }
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
    
class ProduitsListView(ListView):
    queryset=Produit.managed_objects.all()
    template_name='agence/produits.html'
    context_object_name="produits"
    next="home"

    paginate_by=6
    total_number=Produit.objects.all().count()
    pages=ceil(total_number/paginate_by)
    page_range=range(1,pages+1)
    current_page=1

    def get(self, request, *args, **kwargs):
        self.next=resolve(request.path).url_name
        if(request.GET.get('page')):
            self.current_page=int(request.GET.get('page'))
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #contexte pagination
        context["total_number"]=self.total_number
        context["page_range"]=self.page_range
        context["pages"]=self.pages
        context["current_page"]=self.current_page
        
        #contexte généraux à toute les pages
        context['next']=self.next
        context["valeurs"]= list(Valeur.objects.all())
        context["utilitaires"] = Utilitaire.managed_objects.get_last_utilitaire()
        context["valeurs"]= list(Valeur.objects.all())
        context["utiles"]={
            "currency":CURRENCY_UNIT,
        }
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
    


class ProduitViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class=ProduitSerializer
    
    def get_queryset(self):

        queryset=Produit.objects.all()
        id=self.request.GET.get('id')

        if id is not None:
            queryset=queryset.filter(id=id)

        return queryset

class FonctionaliteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class=FonctionaliteSerializer

    def get_queryset(self):

        queryset=Fonctionalite.objects.all()
        id=self.request.GET.get('id')

        if id is not None:
            queryset=queryset.filter(id=id)

        return queryset
