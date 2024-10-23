from django.contrib import admin
from dictionnaire.models import ImageMot, Mot, Source

class MotAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("terme",)}


admin.site.register(Mot,MotAdmin)
admin.site.register(ImageMot)
admin.site.register(Source)
