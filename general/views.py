import pprint
from django.http import Http404

from formulaire.models import *
from .models import Client
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseRedirect
from django.urls import reverse_lazy,resolve
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.views.generic import ListView,RedirectView,DetailView
from django.views.generic.edit import FormView,UpdateView
from banner.models import Banner
from general.constantes import CURRENCY_UNIT
from general.forms import ConnexionForm, InscriptionForm, UpdatePofileForm
from .models import Utilisateur, Utilitaire, Valeur
from django.contrib.auth import authenticate,login,logout
from django.utils.text import slugify


class ConnexionFormView(FormView,SuccessMessageMixin):
    
    template_name="general/connexion.html"
    form_class=ConnexionForm
    success_url='/'
    next="home"
 
    def get(self, request, *args, **kwargs):
        self.next=request.GET.get('next')
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form =self.get_form()
        if form.is_valid():
            
            user=authenticate(request,username=form.cleaned_data['email'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                request.session['user_id']=user.id
                request.session['user_name']=user.username
                request.session['user_mail']=user.email

                self.form_valid(form)
                if request.user.is_superuser:
                    messages.success(request,"Bienvenue %s"%(user.username))
                    if self.next != 'home':
                        return HttpResponseRedirect(reverse_lazy(self.next))
                    else: 
                        return HttpResponseRedirect(reverse_lazy('admin',args=[user.slug]))
                else:
                    if self.next !='home':
                        return HttpResponseRedirect(reverse_lazy(self.next))
                    else:   
                        return HttpResponseRedirect(reverse_lazy('profile',args=[user.slug]))
            else:
                messages.error(request,"Vérifier vos crédentiels et réessayez")
                return super().form_invalid(form)
        else:
            return super().form_invalid(form)

    def form_valid(self, form):
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
     
        #contexte généraux à toute les pages
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
    
class DeconnexionFormView(View):
    
    def get(self,*args, **kwargs):
        logout(self.request)
        return HttpResponseRedirect(reverse_lazy("home"))
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
     
        #contexte généraux à toute les pages
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
    

class UtilisateurDetailView(DetailView):

    template_name="general/profile.html"
    model=Client
    context_name="client"
    profile_owner=False
    slug=""

    def get(self, request, *args, **kwargs):
        #récupération de l'utilisateur en session actuelle
        current_authenticated_user_mail=request.session.get('user_mail')
        self.slug=request.user.slug
        #vérifier si le profile visité correspond à celui de l'utilisateur connecté si non ne pas permettre l'éditon du profile
        if slugify(current_authenticated_user_mail) == self.get_object().slug or request.user.is_superuser:
            self.profile_owner=True

        return super().get(request, *args, **kwargs)

    def get_formulaire(self):
        formulaires=None

        try:
            formulaires=Ecommerce.objects.filter(slug=self.slug)
        except:
            pass
        try:
            formulaires+=Vitrine.objects.filter(slug=self.slug)
        except:
            pass
        try:
            formulaires+=Annuaire.objects.filter(slug=self.slug)
        except:
            pass

       
        return formulaires

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #contexte lié au profile
        context["profile_owner"]=self.profile_owner
        context["formulaires"]=self.get_formulaire()

        #contexte généraux à toute les pages
        context["utilitaires"] = Utilitaire.managed_objects.get_last_utilitaire()
        context["valeurs"]= list(Valeur.objects.all())
        context["utiles"]={
            "currency":CURRENCY_UNIT,
        }
        context["random_banner"]=Banner.objects_random.get_random_banner()
        context["seo"]={
            'title':self.get_object().nom_du_profil,
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

class AdminDetailView(DetailView):

    template_name="general/admin.html"
    queryset=Utilisateur.objects.filter(is_superuser=True)
    context_name="admin"

    def get(self, request, *args, **kwargs):
        
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #contexte lié au profile
        #contexte généraux à toute les pages
        context["utilitaires"] = Utilitaire.managed_objects.get_last_utilitaire()
        context["valeurs"]= list(Valeur.objects.all())
        context["utiles"]={
            "currency":CURRENCY_UNIT,
        }
        context["random_banner"]=Banner.objects_random.get_random_banner()
        context["seo"]={
            'title':self.get_object().username,
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
    

class InscriptionFormView(FormView, SuccessMessageMixin):

    template_name="general/inscription.html"
    form_class=InscriptionForm
    success_url='/'

    def post(self, request, *args, **kwargs):
        
        form =self.get_form()

        if form.is_valid():
            username=form.cleaned_data['username']
            first_name=username.split(' ')[0]
            last_name_list=username.split(' ')[1:]
            last_name=' '.join(last_name_list)
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            password_confirm=form.cleaned_data['password_confirm']
            number=form.cleaned_data['number']
            referenced=form.cleaned_data['referenced']
            fullname="%s %s"%(str(first_name),str(last_name))

            try:
                Utilisateur.objects.get(email=email)
                messages.error(request,"L'Email entré existe déjà")
                return self.form_invalid(form)
            except:
                pass

            try:
                Client.objects.get(username=username)
            except ObjectDoesNotExist:
                try:
                    Client.objects.get(email=email)
                    messages.error(request,'Votre email existe déjà, connectez vous!')
                    return self.form_invalid(form)
                except ObjectDoesNotExist:
                    if password==password_confirm:
                        slug=slugify(email)
                        user=Client.objects.create_user(username=email,email=email,password=password,is_active="True",is_referenced=referenced,slug=slug,numero=number,first_name=first_name,last_name=last_name,nom_du_profil=fullname)
                        login(request,user)
                        request.session['user_id']=user.id
                        request.session['user_name']=user.username
                        request.session['user_mail']=user.email
                        messages.success(request,'Votre compte a été crée avec succès veuillez mettre à jour votre compte')
                        self.form_valid(form)

                        success_url=reverse_lazy('profile',args=[user.slug])
                        return HttpResponseRedirect(reverse_lazy('profile',args=[user.slug]))
                    else:
                        self.form_invalid(form)
                        messages.error(request,'Les mots de passe ne concordent pas')
            
        else:
            return self().form_invalid(form)

    def form_valid(self, form):
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
     
        #contexte généraux à toute les pages
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
    
class ClientUpdateView(UpdateView,SuccessMessageMixin):

    model=Client
    form_class=UpdatePofileForm
    template_name_suffix="_update_form"
    context_name="client"
    
    def post(self, request, *args, **kwargs):
        
        if request.FILES:
            image=request.FILES['photo']
            if image.size <=500000:
                messages.success(request,"Votre profil a bien été mis à jour")
                return super().post(request, *args, **kwargs)
            else:
                messages.error(request,"L'image choisie est trop lourde. Elle doit avoir un poids inférieur à 500 ko actuellement %d ko"%(image.size/1000))
                return HttpResponseRedirect(reverse_lazy('update',args=[self.get_object().slug]))
        else:
            messages.success(request,"Votre profil a bien été mis à jour")
            return super().post(request, *args, **kwargs)

        
    def get(self, request, *args, **kwargs):
        #récupération de l'utilisateur en session actuelle
        current_authenticated_user_mail=request.session.get('user_mail')
        
        #vérifier si le profile visité correspond à celui de l'utilisateur connecté si non ne pas permettre l'éditon du profile
        if slugify(current_authenticated_user_mail) == self.get_object().slug and  not request.user.is_superuser:
            return super().get(request, *args, **kwargs)

        elif request.user.is_superuser:
            return super().get(request, *args, **kwargs)
        
        else:
            raise Http404("Aucune ressource existante")
        
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #contexte généraux à toute les pages
        context["utilitaires"] = Utilitaire.managed_objects.get_last_utilitaire()
        context["valeurs"]= list(Valeur.objects.all())
        context["utiles"]={
            "currency":CURRENCY_UNIT,
        }
        context["random_banner"]=Banner.objects_random.get_random_banner()
        context["seo"]={
            'title':self.get_object().nom_du_profil,
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
