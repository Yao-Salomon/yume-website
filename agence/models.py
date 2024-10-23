from enum import unique
from django.utils import timezone
from django.db import models

class ProduitManager(models.Manager):
    
    def get_last_six_product(self):
        return super().get_queryset().all()[0:6]

    def get_last_two_product(self):
        return super().get_queryset().all()[0:2]
    
    def get_last_product(self):
        return super().get_queryset().all()[1]


class Produit(models.Model):

    badges=(
        ('ruby','Ruby'),
        ('diamant','Diamant'),
        ('or','Or'),
        ('argent','Argent'),
        ('bronze','Bronze'),
    )

    nom=models.CharField("Nom du produit",max_length=250,unique=True)
    icon=models.CharField("icone du produit",max_length=100, default="cart")
    subtitle=models.CharField("Sous titre du produit",max_length=250,unique=True,blank=True,null=True,default=" ")
    badge=models.CharField("Badge du produit",max_length=250,choices=badges)
    date_de_creation=models.DateTimeField("Date d'insertion du produit",default=timezone.now)
    old_price=models.CharField("Prix original du produit",max_length=50,default="")
    price=models.CharField("Prix du produit",max_length=50,default="")
   
    objects=models.Manager()
    managed_objects=ProduitManager()

    def __str__(self):
        return "%s %s"%(self.nom,self.subtitle )
    
    def get_fonctionalite(self):

        return self.fonctionalite_set.all()

    class Meta:
        verbose_name="Produit de l'Agence"
        verbose_name_plural="Liste des Produits de l'Agence "
        ordering=['-date_de_creation']

class Fonctionalite(models.Model):

    nom=models.CharField("Non de la fonctionnalité",max_length=250)
    inclusion=models.BooleanField("Fonctionalité incluse ou non?",default=True)
    nombre=models.CharField("Nombre d'inclusion de la fonctionnalité",max_length=100,null=True,blank=True)
    produit=models.ManyToManyField(Produit)
    icon=models.CharField("icone du produit",max_length=100, default="dpad")


    def __str__(self):
        return "%s %s %s"%(self.nom,self.nombre,str(self.inclusion))

class Services(models.Model):
    nom=models.CharField("Nom du service",max_length=250,unique=True)
    description=models.TextField("Description du service",default=" ")

    def __str__(self):
        return self.nom

