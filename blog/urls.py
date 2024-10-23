from django.urls import path
from blog.views import BilletDetailView, BilletPreviewDetailView, BlogListView, PartieDetailView


urlpatterns = [

    path('',BlogListView.as_view(),name="blog"),
    path('<slug:slug>',BilletDetailView.as_view(),name="billet"),
    path('preview/<slug:slug>',BilletPreviewDetailView.as_view(),name="preview"),
    path('partie/<slug:slug>',PartieDetailView.as_view(),name="partie"),

]