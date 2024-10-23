from django.views.generic import DetailView,ListView
from django.urls import resolve
from banner.models import Banner
from general.constantes import CURRENCY_UNIT
from general.models import Utilitaire, Valeur
from .models import Mot
from math import ceil


class MotDetailView(DetailView):
    template_name='dictionnaire/mot.html'
    context_name='mot'
    next="dictionnaire"

    def get(self, request, *args, **kwargs):
        self.next=resolve(request.path).url_name
        return super().get(request, *args, **kwargs)
    
    def get_object(self, queryset=Mot.objects.all()):
        mot=super().get_object(queryset)
        mot.purify()
        return mot

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
            'title':self.get_object().terme,
            'category':"Article de Blog",
            'description':self.get_object().definition[0:150],
            'robots':None,
            'keywords':"Yume, Blog, Création de site internet, SEO"+self.get_object().definition[0:10],
            'schema':None,
        }
        context['og']={
            'title':self.get_object().terme,
            'site-name':"Yume",
            'descritpion':self.get_object().definition[0:50],
            'url':self.request.build_absolute_uri,
            'type':"Website",
            'image':None,
        }
        #contextspécifique
        context['carousels']=list(self.get_object().get_photo())
        context['has_photo']=len(list(self.get_object().get_photo()))!=0
        context['sources']=list(self.get_object().get_source())
        return context
    

class MotListView(ListView):
    template_name='dictionnaire/index.html'
    context_object_name="mots"
    next="dictionnaire"
    paginate_by=50
    total_number=Mot.objects.all().count()
    pages=ceil(total_number/paginate_by)
    page_range=range(1,pages+1)
    current_page=1
    
    def get(self, request, *args, **kwargs):
        self.next=resolve(request.path).url_name
        if(request.GET.get('page')):
            self.current_page=int(request.GET.get('page'))
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset=Mot.objects.all().order_by('terme')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #contexte pagination
        context["total_number"]=self.total_number
        context["page_range"]=self.page_range
        context["pages"]=self.pages
        context["current_page"]=self.current_page

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
    
