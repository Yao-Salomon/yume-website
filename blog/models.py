from django.db import models
from django.urls import reverse
from django.utils import timezone
from general.regex import *


class BilletManager(models.Manager):

    def get_published_billet(self):
        pass
    
        queryset=super().get_queryset().filter(publier=True)
        for billet in queryset:
            billet.purify()
        return queryset
        
    def get_queryset(self):
        return self.get_published_billet()

    def get_last_billet(self):
        return self.get_published_billet()[1]
    
    def get_last_six_billet(self):
        return self.get_published_billet()[0:6]

class Billet(models.Model):
    titre=models.CharField("titre du billet",max_length=250)
    icon=models.CharField("Icône du billet",max_length=100,default="newspaper")
    slug=models.SlugField("slug du blog",max_length=250)
    introduction=models.TextField("Introduction du billet")
    image_introduction=models.ImageField("Image de l'introduction",upload_to="blog/%Y",blank=True,null=True)
    conclusion=models.TextField("Conclusion du blog")
    image_conclusion=models.ImageField("Image de l'conclusion",upload_to="blog/%Y",blank=True,null=True)
    date_de_creation=models.DateTimeField("Date de création",default=timezone.now)
    publier=models.BooleanField("Publier ?",default=False)
    auteur=models.CharField("Auteur du billet",default="Yume",max_length=250)

    class Meta:
        ordering=['-date_de_creation']
        verbose_name="Billet de Blog"
        verbose_name_plural="Billets de blog"

    objects=models.Manager()
    managed_objects=BilletManager()

    def get_absolute_url(self):
        return reverse("billet", kwargs={"slug": self.slug})
    
    def purify(self):

        self.introduction=gras.sub(r" <span class='fw-bold'> ",self.introduction)
        self.introduction=grasf.sub(r" </span> ",self.introduction)

        self.introduction=iliste.sub(r" <ul class='text-start'> ",self.introduction)
        self.introduction=ilistef.sub(r" </ul> ",self.introduction)

        self.introduction=iaccent.sub(r" <span class='text-primary fw-bolder'> ",self.introduction)
        self.introduction=iaccentf.sub(r" </span> ",self.introduction)

        self.introduction=ibulle.sub(r" <li> ",self.introduction)
        self.introduction=ibullef.sub(r" </li> ",self.introduction)

        self.introduction=ytalique.sub(r" <span class='fst-italic'> ",self.introduction)
        self.introduction=ytaliquef.sub(r" </span> ",self.introduction)

        self.conclusion=gras.sub(r" <span class='fw-bold'> ",self.conclusion)
        self.conclusion=grasf.sub(r" </span> ",self.conclusion)

        self.conclusion=ytalique.sub(r" <span class='fst-italic'> ",self.conclusion)
        self.conclusion=ytaliquef.sub(r" </span> ",self.conclusion)

        self.conclusion=iliste.sub(r" <ul class='text-start'> ",self.conclusion)
        self.conclusion=ilistef.sub(r" </ul> ",self.conclusion)

        self.conclusion=iaccent.sub(r" <span class='text-primary fw-bolder'> ",self.conclusion)
        self.conclusion=iaccentf.sub(r" </span> ",self.conclusion)

        self.conclusion=ibulle.sub(r" <li> ",self.conclusion)
        self.conclusion=ibullef.sub(r" </li> ",self.conclusion)

    
    def __str__(self):
        return self.titre

class Partie(models.Model):
    titre=models.CharField("Titre de la partie",max_length=250)
    contenu=models.TextField("Contenu de la parite")
    billet=models.ForeignKey(Billet,on_delete=models.CASCADE)
    image1=models.ImageField("Image 1",upload_to="blog/%Y",blank=True,null=True)
    image2=models.ImageField("Image 2",upload_to="blog/%Y",blank=True,null=True)
    image3=models.ImageField("Image 3",upload_to="blog/%Y",blank=True,null=True)
    image4=models.ImageField("Image 4",upload_to="blog/%Y",blank=True,null=True)
    publier=models.BooleanField("Publier ?",default=False)
    slug=models.SlugField("Slug pour les liens",max_length=250)

    def purify(self):

        self.contenu=gras.sub(r" <span class='fw-bold'> ",self.contenu)
        self.contenu=grasf.sub(r" </span> ",self.contenu)

        self.contenu=iliste.sub(r" <ul class='text-start'> ",self.contenu)
        self.contenu=ilistef.sub(r" </ul> ",self.contenu)

        self.contenu=iaccent.sub(r" <span class='text-primary fw-bolder'> ",self.contenu)
        self.contenu=iaccentf.sub(r" </span> ",self.contenu)

        self.contenu=ibulle.sub(r" <li> ",self.contenu)
        self.contenu=ibullef.sub(r" </li> ",self.contenu)

        self.contenu=ytalique.sub(r" <span class='fst-italic'> ",self.contenu)
        self.contenu=ytaliquef.sub(r" </span> ",self.contenu)

        if self.image1 :
            self.contenu=image1.sub(r"<div class='d-flex justify-content-center'><img class='img-fluid' style='max-height: 400px; max-width:400px' src='{0}' alt='je test mon atrribut alt'> </div>".format(self.image1.url),self.contenu)
        if self.image2 :
            self.contenu=image2.sub(r"<div class='d-flex justify-content-center'><img class='img-fluid' style='max-height: 500px; max-width:500px' src='{0}' alt='je test mon atrribut alt'> </div>".format(self.image2.url),self.contenu)
        if self.image3 :
            self.contenu=image3.sub(r"<div class='d-flex justify-content-center'><img class='img-fluid' style='max-height: 400px; max-width:400px' src='{0}' alt='je test mon atrribut alt'> </div>".format(self.image3.url),self.contenu)
        if self.image4 :
            self.contenu=image4.sub(r"<div class='d-flex justify-content-center'><img class='img-fluid' style='max-height: 500px; max-width:500px' src='{0}' alt='je test mon atrribut alt'> </div>".format(self.image4.url),self.contenu)
 

       
    
    def get_absolute_url(self):
        return reverse("partie", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.titre

class CommentaireManager(models.Manager):

    def total(self):
        return super().get_queryset().all().count()

class Commentaire(models.Model):
    pseudo=models.CharField("pseudo",max_length=250)
    avatar=models.ImageField("avatar",upload_to="blog/avatars",blank=True,null=True)
    contenu=models.TextField("contenu du commentaire")
    visiteur=models.CharField("adresse ip du visiteur",max_length=250)
    billet=models.ForeignKey(Billet,on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s"%(self.pseudo, self.contenu[0:1])

class ReponsesCommentaire(models.Model):
    pseudo=models.CharField('votre pseudo',max_length=200)
    contenu=models.TextField('votre commentaire',max_length=200)
    date=models.DateTimeField('date',default=timezone.now)
    commentaire=models.ForeignKey(Commentaire,on_delete=models.CASCADE)

    def __str__(self):
        return self.pseudo