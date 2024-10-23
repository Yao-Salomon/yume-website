from django.urls import reverse
from django.db.models.functions import Lower
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class DescriptionManager(models.Manager):

    def get_last_description(self):
        queryset = super().get_queryset().order_by('-release_date')
        if queryset.exists():
            return queryset[0]
        return None 

class Description(models.Model):

    contenu=models.TextField("description",default="Acune description enregistrée")
    release_date=models.DateField('date de mise en ligne',default=timezone.now)
    
    #manager
    managed_objects=DescriptionManager()

    class Meta:
        verbose_name="Présentation de l'entreprise"
        verbose_name_plural="Présentations de l'entreprise "
        ordering=['-release_date']
    
    def __str__(self):
        return "description du %s"%(str(self.release_date))

class MotDirecteurManager(models.Manager):

    def get_last_mot(self):
        queryset = super().get_queryset().order_by('-release_date')
        if queryset.exists():
            return queryset[0]
        return None

class MotDirecteur(models.Model):

    contenu=models.TextField("mot du directeur",default=" ")
    release_date=models.DateField('date de mise en ligne',default=timezone.now)
    
    #manager
    managed_objects=MotDirecteurManager()

    class Meta:
        verbose_name="Mot du Directeur"
        verbose_name_plural="Mots du Directeur "
        ordering=['-release_date']
    
    def __str__(self):
        return "Mot du Directeur du %s"%(str(self.release_date))

class Team(models.Model):

    nom=models.CharField("nom",max_length=250)
    prenom=models.CharField("prénom(s)",max_length=250)
    description=models.TextField("description",default="Acune description enregistrée")
    numero=models.CharField("numéro de téléphone",max_length=100,default="Aucun numéro enregistré")
    creation_date=models.DateField("date de création",)

class Temoignage(models.Model):

    nom=models.CharField(_("Nom"), max_length=200)
    organisation=models.CharField(_("Organisation"), max_length=100)
    contenu=models.TextField(_("Contenu du témoignage"))
    date=models.DateField(_("Date de témoignage"),default=timezone.now, auto_now=False, auto_now_add=False)
    publier=models.BooleanField(_("Le témoignage doit-il être publier"),default=False)    

    class Meta:
        verbose_name = _("Temoignage")
        verbose_name_plural = _("Temoignages")

    def __str__(self):
        return self.organisation

    def get_absolute_url(self):
        return reverse("Temoignage_detail", kwargs={"pk": self.pk})

class Historique(models.Model):
    pass
