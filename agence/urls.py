from django.urls import path
from about.views import AboutTemplateView, ContactTemplateView, TeamListView
from .views import ClientListView, ProduitsListView

urlpatterns = [

    path('',ClientListView.as_view(),name="annuaire"),
    path('presentation',ContactTemplateView.as_view(),name="contacts"),
    path('equipe-de-yume',TeamListView.as_view(),name="team"),
    path('produits',ProduitsListView.as_view(),name="produits"),

]