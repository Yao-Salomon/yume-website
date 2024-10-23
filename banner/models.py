from operator import mod
from django.db import models
from django.utils import timezone
from django.urls import reverse
import random

class BannerManager(models.Manager):

    def get_random_banner(self):

        total=super().get_queryset().all().count()

        if int(total) != 0:
            number=random.randint(1,int(total))
            return super().get_queryset().get(id=number)
        else:
            return "Aucun objet n'a encore été enregistré"


class Banner(models.Model):
    message=models.CharField("message de la bannière",max_length=250)
    date_de_publication=models.DateTimeField("date de la publication du message",default=timezone.now)

    #managers
    objects_random=BannerManager()

    def __str__(self):
        return self.message

    class Meta:
        ordering=['-date_de_publication']
        verbose_name="Message de la bannière"
        verbose_name_plural="Messages de la bannière"


class CarouselManager(models.Manager):
    
    def get_publicated(self):
        return super().get_queryset().filter(state=True)

class Carousel(models.Model):

    categorie=(
        ('evenement',"évènement"),
        ('billet',"billet de blog"),
        ('livre',"livre"),
        ('news',"news"),
        ('technique','technique')

    )
    image=models.ImageField("image du carousel",upload_to="carousel")
    categorie=models.CharField("catégorie du carousel",max_length=250,choices=categorie)
    titre=models.CharField("titre du carousel",max_length=250)
    date_de_publication=models.DateTimeField("date de publication",default=timezone.now)
    state=models.BooleanField("état de publication")
    texte=models.CharField("texte brève decrivant le carousel",max_length=250,default="Aucun texte descriptif")
    slug=models.SlugField("Slug pour le lien",max_length=250)

    #managers
    publicated_objects=CarouselManager()

    def __str__(self):
        return self.titre
    
    class Meta:
        ordering=['-date_de_publication']
        verbose_name="Element du carousel"
        verbose_name_plural="Elements du carousel"
