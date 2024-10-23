from django.contrib import admin

from banner.models import Banner, Carousel

class BannerAdmin(admin.ModelAdmin):
    pass
class CarouselAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("titre",)}

admin.site.register(Banner,BannerAdmin)
admin.site.register(Carousel, CarouselAdmin)
