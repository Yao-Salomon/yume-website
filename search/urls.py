from django.urls import path
from .views import SearchListView, SearchDetailView, SearchTemplateView

urlpatterns = [

    path('',SearchTemplateView.as_view(),name="home"),
    path('results',SearchListView.as_view(),name="resultat"),
    path('membre/<slug:slug>',SearchDetailView.as_view(),name="member"),

]