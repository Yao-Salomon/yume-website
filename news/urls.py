from django.urls import path
from about.views import AboutTemplateView, ContactTemplateView, TeamListView


urlpatterns = [

    path('',AboutTemplateView.as_view(),name="news"),
    path('presentation',ContactTemplateView.as_view(),name="contacts"),
    path('equipe-de-yume',TeamListView.as_view(),name="team"),

]