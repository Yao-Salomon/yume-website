from django.db import models
from blog.models import Billet
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CommentaireManager(models.Manager):

    def total(self):
        return super().get_queryset().all().count()

class CommentaireBlog(models.Model):
    contenu=models.TextField("contenu du commentaire")
    date=models.DateTimeField('date',default=timezone.now)
    user=models.ForeignKey("general.Utilisateur", verbose_name=_("Utilisateur"), on_delete=models.CASCADE)
    billet=models.ForeignKey(Billet,on_delete=models.CASCADE)

    managed_objects=CommentaireManager()

    def __str__(self):
        return "%s %s"%(self.user, self.contenu[0:4])

class ReponsesCommentaire(models.Model):
    contenu=models.TextField('votre commentaire',max_length=200)
    date=models.DateTimeField('date',default=timezone.now)
    user=models.ForeignKey("general.Utilisateur", verbose_name=_("Utilisateur"), on_delete=models.CASCADE)
    commentaire=models.ForeignKey(CommentaireBlog,on_delete=models.CASCADE)
    
    managed_objects=CommentaireManager()

    def __str__(self):
        return "%s %s"%(self.user, self.contenu[0:4])