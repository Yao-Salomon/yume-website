from django.contrib import admin
from .models import *

#model admin
class DescriptionAdmin(admin.ModelAdmin):
    pass

class MotDirecteurAdmin(admin.ModelAdmin):
    pass

class TeamAdmin(admin.ModelAdmin):
    view_on_site=True

class HistoriqueAdmin(admin.ModelAdmin):
    pass

#registering admin site
admin.site.register(Description,DescriptionAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Historique,HistoriqueAdmin)
admin.site.register(MotDirecteur,MotDirecteurAdmin)
admin.site.register(Temoignage)