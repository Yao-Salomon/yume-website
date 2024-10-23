from django.urls import path
from .views import AdminDetailView, ClientUpdateView, ConnexionFormView, DeconnexionFormView, InscriptionFormView, UtilisateurDetailView
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('connexion',ConnexionFormView.as_view(),name="connexion"),
    path('deconnexion',DeconnexionFormView.as_view(),name="deconnexion"),
    path('inscription',InscriptionFormView.as_view(),name="inscription"),
    path('profiles/<slug:slug>',login_required(UtilisateurDetailView.as_view()),name="profile"),
    path('profiladministration/<slug:slug>',login_required(AdminDetailView.as_view()),name="admin"),
    path('profileupdate/<slug:slug>',login_required(ClientUpdateView.as_view()),name="update"),

]
