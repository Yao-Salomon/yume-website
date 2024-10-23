from django.db import models
from general.regex import *
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Mot(models.Model):
    terme=models.CharField("Mot défini",max_length=250,help_text="Entrez le mot à définir")
    definition=models.TextField("Définition du mot",help_text="Entrez la définition du mot en détaillant le plus possible (vous pouvez utilisez les outils de codification )")
    slug=models.SlugField("Slug pour le référencement",help_text="Entrez un slug valide pour le référencement du mot sur le web")
    
    def purify(self):

        self.definition=gras.sub(r" <span class='fw-bold'> ",self.definition)
        self.definition=grasf.sub(r" </span> ",self.definition)

        self.definition=iliste.sub(r" <ul class='text-start'> ",self.definition)
        self.definition=ilistef.sub(r" </ul> ",self.definition)

        self.definition=iaccent.sub(r" <span class='text-primary fw-bolder'> ",self.definition)
        self.definition=iaccentf.sub(r" </span> ",self.definition)

        self.definition=ibulle.sub(r" <li> ",self.definition)
        self.definition=ibullef.sub(r" </li> ",self.definition)

        self.definition=ytalique.sub(r" <span class='fst-italic'> ",self.definition)
        self.definition=ytaliquef.sub(r" </span> ",self.definition)
    
    def get_photo(self):
    
        return self.imagemot_set.all()

    def get_source(self):
    
        return self.source_set.all()

    def get_absolute_url(self):
        return reverse("definition", kwargs={"slug": self.slug})


    def __str__(self):
        return self.terme

class ImageMot(models.Model):
    photo=models.ImageField(_("Photo descriptif du mot"), upload_to="dictionnaire/mot/%Y")
    publier=models.BooleanField(_("La Photo doit-elle être publier"))
    credit=models.CharField(_("Credit de la photo"), max_length=50,null=True,blank=True)
    mot=models.ForeignKey("dictionnaire.Mot", verbose_name=_("mot lié à la photo"), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("ImageMot")
        verbose_name_plural = _("ImageMots")

    def __str__(self):
        return "photo %d du terme %s"%(self.id,self.mot.terme)

    def get_absolute_url(self):
        return reverse("ImageMot_detail", kwargs={"pk": self.pk})

class Source(models.Model):
    auteur=models.CharField(_("Nom de l'auteur ou des auteurs de la source"), max_length=250)
    nom=models.CharField(_("Titre du livre ou nom de l'article de parution du mot"), max_length=100)
    year=models.CharField(_("Annee de la publication"), max_length=6)
    site=models.URLField(_("Url du site web de la publication"), max_length=200)
    mot=models.ForeignKey("dictionnaire.Mot", verbose_name=_("mot lié à la source"), on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("Source")
        verbose_name_plural = _("Sources")

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("Source_detail", kwargs={"pk": self.pk})
