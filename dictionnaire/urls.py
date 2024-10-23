from django.urls import path
from .views import MotDetailView,MotListView


urlpatterns = [

    path('',MotListView.as_view(),name="dictionnaire"),
    path('<slug:slug>',MotDetailView.as_view(),name="mot"),
]