from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from banner.models import Banner
from dictionnaire.models import Mot
from formulaire.models import Ecommerce, Vitrine,Blog
from general.constantes import CURRENCY_UNIT
from general.forms import BlogCreateForm, EcommerceCreateForm, VitrineCreateForm
from general.models import TypeFormulaire, Utilitaire, Valeur
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.messages.views import SuccessMessageMixin
import datetime
from http import client
from django.http import HttpRequest
from django.urls import resolve

import http.client, urllib.request, urllib.parse, urllib.error, base64

"""
try:
    conn = http.client.HTTPConnection('127.0.0.1',port=8000)
    conn.request("GET","/")
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print(e.__str__())
"""
date_actuelle=datetime.date.today()
delta=datetime.timedelta(days=15)
date_butoire=date_actuelle+delta

class FormListView(TemplateView):
    template_name="formulaire/index.html"
    context_name="formulaires"
    next="home"

    def get(self, request, *args, **kwargs):
        self.next=resolve(request.path).url_name
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #contexte lié à la vue courante
        context["type_formulaires"]=TypeFormulaire.objects.filter(is_available=True)

        #contexte généraux à toute les pages
        context['termes']=list(Mot.objects.all())
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
    
class EcommerceCreateView(CreateView,SuccessMessageMixin):
    model=Ecommerce
    form_class=EcommerceCreateForm
    template_name_suffix="_create_form"
    context_name="ecommerce"
    initial={}
    success_url=""
    next="home"

    def get(self, request, *args, **kwargs):
        username="%s %s"%(str(request.user.first_name),str(request.user.last_name))
        mail="%s"%(str(request.user.email))
        numero="%s"%(str(request.user.numero))
        slug="%s"%(str(request.user.slug))
        self.next=resolve(request.path).url_name

        self.initial={
            "username":username,
            "mail":mail,
            "numero":numero,
            "slug":slug,
            "date_butoire":date_butoire.isoformat(),
        }
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form=self.get_form()

        slug="%s"%(str(request.user.slug))
        if request.user.is_staff:
            self.success_url=reverse_lazy("admin", kwargs={"slug":slug })
        else:
            self.sucess_url=reverse_lazy("profile", kwargs={"slug":slug })
        
        return super().post(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #contexte lié à la vue courante
        context["type_formulaires"]=TypeFormulaire.objects.filter(is_available=True)

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
      
class EcommerceUpdateView(UpdateView,SuccessMessageMixin):
    model=Ecommerce
    form_class=EcommerceCreateForm
    template_name_suffix="_update_form"
    context_name="ecommerce"
    success_url=""
    initial={}
    next="home"
    
    def get(self, request, *args, **kwargs):
        formulaire=super().get_object()
        self.initial={
            "date_butoire":formulaire.date_butoire.isoformat(),
        }
        self.next=resolve(request.path)
        return super().get(request, *args, **kwargs)

        
    def post(self, request, *args, **kwargs):
        form=self.get_form()
        slug="%s"%(str(request.user.slug))
        if request.user.is_staff:
            self.success_url=reverse_lazy("admin", kwargs={"slug":slug })
        else:
            self.sucess_url=reverse_lazy("profile", kwargs={"slug":slug })
        
        if form.is_valid():
            messages.success(request,"Votre réponse au formulaire a bien été enregistré")

        return super().post(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #contexte lié à la vue courante
        context["type_formulaires"]=TypeFormulaire.objects.filter(is_available=True)

        #contexte généraux à toute les pages
        context['termes']=list(Mot.objects.all())
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
  
class VitrineCreateView(CreateView,SuccessMessageMixin):
    model=Vitrine
    form_class=VitrineCreateForm
    template_name_suffix="_create_form"
    context_name="vitrine"
    initial={}
    success_url=""
    next="formulaires"

    def get(self, request, *args, **kwargs):
        username="%s %s"%(str(request.user.first_name),str(request.user.last_name))
        mail="%s"%(str(request.user.email))
        numero="%s"%(str(request.user.numero))
        slug="%s"%(str(request.user.slug))
        self.next=resolve(request.path).url_name

        self.initial={
            "username":username,
            "mail":mail,
            "numero":numero,
            "slug":slug,
            "date_butoire":date_butoire.isoformat(),
        }
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form=self.get_form()

        slug="%s"%(str(request.user.slug))
        if request.user.is_staff:
            self.success_url=reverse_lazy("admin", kwargs={"slug":slug })
        else:
            self.sucess_url=reverse_lazy("profile", kwargs={"slug":slug })
        
        return super().post(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #contexte lié à la vue courante
        context["type_formulaires"]=TypeFormulaire.objects.filter(is_available=True)

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

class VitrineUpdateView(UpdateView,SuccessMessageMixin):
    model=Vitrine
    form_class=VitrineCreateForm
    template_name_suffix="_update_form"
    context_name="vitrine"
    initial={}
    success_url=""
    next="formulaires"

    def get(self, request, *args, **kwargs):
        username="%s %s"%(str(request.user.first_name),str(request.user.last_name))
        mail="%s"%(str(request.user.email))
        numero="%s"%(str(request.user.numero))
        slug="%s"%(str(request.user.slug))
        self.next=resolve(request.path).url_name

        self.initial={
            "username":username,
            "mail":mail,
            "numero":numero,
            "slug":slug,
            "date_butoire":date_butoire.isoformat(),
        }
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form=self.get_form()

        slug="%s"%(str(request.user.slug))
        if request.user.is_staff:
            self.success_url=reverse_lazy("admin", kwargs={"slug":slug })
        else:
            self.sucess_url=reverse_lazy("profile", kwargs={"slug":slug })
        
        return super().post(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #contexte lié à la vue courante
        context["type_formulaires"]=TypeFormulaire.objects.filter(is_available=True)

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
  
class BlogCreateView(CreateView,SuccessMessageMixin):
    model=Blog
    form_class=BlogCreateForm
    template_name_suffix="_create_form"
    context_name="blog"
    initial={}
    success_url=""
    next="formulaires"

    def get(self, request, *args, **kwargs):
        username="%s %s"%(str(request.user.first_name),str(request.user.last_name))
        mail="%s"%(str(request.user.email))
        numero="%s"%(str(request.user.numero))
        slug="%s"%(str(request.user.slug))
        self.next=resolve(request.path).url_name

        self.initial={
            "username":username,
            "mail":mail,
            "numero":numero,
            "slug":slug,
            "date_butoire":date_butoire.isoformat(),
        }
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form=self.get_form()

        slug="%s"%(str(request.user.slug))
        if request.user.is_staff:
            self.success_url=reverse_lazy("admin", kwargs={"slug":slug })
        else:
            self.sucess_url=reverse_lazy("profile", kwargs={"slug":slug })
        
        return super().post(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #contexte lié à la vue courante
        context["type_formulaires"]=TypeFormulaire.objects.filter(is_available=True)

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

class BlogUpdateView(UpdateView,SuccessMessageMixin):
    model=Blog
    form_class=BlogCreateForm
    template_name_suffix="_update_form"
    context_name="blog"
    initial={}
    success_url=""
    next="formulaires"

    def get(self, request, *args, **kwargs):
        username="%s %s"%(str(request.user.first_name),str(request.user.last_name))
        mail="%s"%(str(request.user.email))
        numero="%s"%(str(request.user.numero))
        slug="%s"%(str(request.user.slug))
        self.next=resolve(request.path).url_name

        self.initial={
            "username":username,
            "mail":mail,
            "numero":numero,
            "slug":slug,
            "date_butoire":date_butoire.isoformat(),
        }
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form=self.get_form()

        slug="%s"%(str(request.user.slug))
        if request.user.is_staff:
            self.success_url=reverse_lazy("admin", kwargs={"slug":slug })
        else:
            self.sucess_url=reverse_lazy("profile", kwargs={"slug":slug })
        
        return super().post(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #contexte lié à la vue courante
        context["type_formulaires"]=TypeFormulaire.objects.filter(is_available=True)

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
  

class LoginTemplateView(TemplateView):
    pass