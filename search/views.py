from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from about.models import Description, MotDirecteur
from agence.models import Produit
from banner.models import Banner, Carousel
from blog.models import Billet
from dictionnaire.models import Mot
from general.constantes import CURRENCY_UNIT
from general.models import Temoignage, Utilitaire, Valeur
from django.urls import resolve

class SearchTemplateView(TemplateView):

    template_name="search/index.html"
    next="home"

    def get(self, request, *args, **kwargs):
        self.next=resolve(request.path).url_name
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #context spécifique à la page
        context["carousels"]=list(Carousel.publicated_objects.get_publicated())
        context["temoignages"]=list(Temoignage.objects.all())
        context["produits"]=list(Produit.managed_objects.get_last_six_product())
        context["blog"]=list(Billet.managed_objects.get_last_six_billet())
        context["presentation"]=Description.managed_objects.get_last_description()
        context["directeur"]=MotDirecteur.managed_objects.get_last_mot()
        
        #contexte généraux à toute les pages
        context['next']=self.next
        context['termes']=list(Mot.objects.all())
        context["utilitaires"] = Utilitaire.managed_objects.get_last_utilitaire()
        context["valeurs"]= list(Valeur.objects.all())
        context["utiles"]={
            "currency":CURRENCY_UNIT,
        }
        context["random_banner"]=Banner.objects_random.get_random_banner()
        context["seo"]={
            'title':None,
            'category':None,
            'description':None,
            'robots':None,
            'keywords':None,
            'schema':None,
        }
        context['og']={
            'title':None,
            'site-name':None,
            'descritpion':None,
            'url':None,
            'type':None,
            'image':None,
        }
        
        return context
    

class SearchListView(ListView):
    pass

class SearchDetailView(DetailView):
    pass
