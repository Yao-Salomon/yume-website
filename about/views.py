from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from about.models import Description, MotDirecteur, Temoignage
from banner.models import Banner
from dictionnaire.models import Mot
from general.constantes import CURRENCY_UNIT
from general.models import Utilitaire, Valeur

class AboutTemplateView(TemplateView):
    template_name="about/about.html"
    next="home"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #contexte lié à la page présente
        context["presentation"]=Description.managed_objects.get_last_description()
        context["directeur"]=MotDirecteur.managed_objects.get_last_mot()
        context["carousels"]=list(Temoignage.objects.filter(publier=True))
        
        #contexte généraux à toute les pages
        context["utilitaires"] = Utilitaire.managed_objects.get_last_utilitaire()
        context["valeurs"]= list(Valeur.objects.all())
        context['termes']=list(Mot.objects.all())
        context["utiles"]={
            "currency":CURRENCY_UNIT,
        }
        context['next']=self.next
        context["random_banner"]=Banner.objects_random.get_random_banner()
        context["seo"]={
            'title':"A propos | Yume, Votre solution digital-création d'applications web et mobile",
            'category':"Blog, Site internet, Applications Web, Applications mobiles, référencement organique",
            'description':"Yume vous apporte le meilleur du digital à Abidjan, Yamoussoukro et partout ailleurs en Côte D'Ivoire.",
            'robots':None,
            'keywords':"Yume,création de vos applications, CMS, applications Web en Côte d'Ivoire, Côte D'Ivoire, Côte D'Ivoire, Yume Abidjan, Yume, Yume Yamoussoukro, Application Web, Application Mobile",
            'schema':"",
        }
        context['og']={
            'title':"A propos | Yume, Votre solution digital-création d'applications web et mobile",
            'site-name':"Yume",
            'description':"Yume vous apporte le meilleur du digital à Abidjan, Yamoussoukro et partout ailleurs en Côte D'Ivoire.",
            'url':self.request.build_absolute_uri,
            'type':"Website",
            'image':None,
        }

        
        return context
    


class TeamListView(ListView):
    template_name="about/team.html"
    pass

class ContactTemplateView(TemplateView):
    template_name="about/contact.html"
