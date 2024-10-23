
from django.urls import path
from .views import *

urlpatterns = [
    path("login",LoginTemplateView.as_view(),name="form_login"),
    path("",FormListView.as_view(),name="formulaires"),
    path("ecommerce",EcommerceCreateView.as_view(),name="ecommerce"),
    path("ecommerce/<int:pk>",EcommerceUpdateView.as_view(),name="ecommerce_update"),
    path("vitrine",VitrineCreateView.as_view(),name="vitrine"),
    path("vitrine/<int:pk>",VitrineUpdateView.as_view(),name="vitrine_update"),
     path("blogform",BlogCreateView.as_view(),name="blogform"),
    path("blogform/<int:pk>",BlogUpdateView.as_view(),name="blogform_update"),

]
