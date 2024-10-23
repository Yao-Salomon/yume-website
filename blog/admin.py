from django.contrib import admin
from .models import Billet,Commentaire,Partie

class PartieAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("titre",)}


class BilletAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("titre",)}

admin.site.register(Billet,BilletAdmin)
admin.site.register(Partie,PartieAdmin)
