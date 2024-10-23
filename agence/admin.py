from django.contrib import admin

from agence.models import Fonctionalite, Produit

class ProduitAdmin(admin.ModelAdmin):
    pass

class FonctionaliteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Produit,ProduitAdmin)
admin.site.register(Fonctionalite,FonctionaliteAdmin)
