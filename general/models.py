from email.mime import image
from email.policy import default
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.urls import reverse
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _

class MyUserManager(BaseUserManager):
    def create_user(self, email, slug, password=None):
        
        if not email:
            raise ValueError('Les utilisateurs doivent avoir un email')

        user = self.model(
            email=self.normalize_email(email),
            slug=slug,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, slug, password):
       
        user = self.create_user(email,
            password=password,
            slug=slug
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Utilisateur(AbstractUser):

    numero=models.CharField("numéro de téléphone",max_length=100,default="Aucun numéro enregistré")
    adresse=models.CharField("adresse de l'utilisateur ",max_length=250,default="Aucune adresse enregistrée")
    is_referenced=models.BooleanField("l'utilisateur est-il referencé ?",default=False)
    slug=models.SlugField("champ automatique généré pour le référecement",max_length=250)
    stars=models.IntegerField("Nombre d'étoiles pour le positionnement",default=0)
    email = models.EmailField(
        verbose_name="Adresse email",
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(_("L'utilisateur est-il actif?"),default=True)
    is_admin = models.BooleanField(_("L'utilisateur est-il administrateur du site?"),default=False)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['slug']
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name="Utilisateur"
        verbose_name_plural="Liste des Utilisateurs"
    
    def get_absolute_url(self):
        return reverse("utilisateur", kwargs={"slug":self.slug })
    
    def __str__(self):
        return self.username

class Activite(models.Model):

    nom=models.CharField("Nom de l'activité",max_length=200)
    icone=models.CharField("Icône de l'activité ",max_length=200,default="bag-fill")
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name="Activité"
        verbose_name_plural="Activités"

class Client(Utilisateur):

    about=models.TextField("Description détaillée",default="Acune description n'a encore été ajoutée")
    siteweb=models.CharField("url du site web",default="https://www.yume.ci",max_length=250)
    nom_du_profil=models.CharField("nom du profil",max_length=250,default="Aucun nom de profil enregistré")
    photo=models.ImageField("Photo de profile",upload_to="clients/%Y",null=True,blank=True)
    activite=models.ManyToManyField(Activite)

    def get_activite(self):

        return self.activite.all()

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug":self.slug })

    class Meta:
        verbose_name="Client"
        verbose_name_plural="Clients"

class UtilitaireManager(models.Manager):

    def get_last_utilitaire(self):
        queryset=super().get_queryset().order_by(Lower('last_modification').desc())
        if(queryset.exists()):
            return queryset[0]
        return None

class Utilitaire(models.Model):
    
    titre_barre_de_recherche=models.CharField("titre de la barre de recherche page d'accueil",max_length=250,default="faites une recherche sur Yume")
    slogan=models.CharField("slogan",max_length=250,default="donnez vous le droit de rêvez")
    slogan_reduit=models.CharField("slogan réduit pour petit écran",max_length=250,default="Rêvez")
    home_image=models.ImageField("Image de la page d'Accueil",upload_to="utilitaire")
    last_modification=models.DateTimeField("Date de la dernière modification",default=timezone.now)
    
    #manager
    managed_objects=UtilitaireManager()

    class Meta:
        verbose_name="Utilitaire"
        verbose_name_plural="Liste des Utilitaires"
    
    def __str__(self):
        return str(self.last_modification)

class Temoignage(models.Model):
    contenu=models.TextField("Contenu du témoignage")
    auteur=models.CharField("Auteur du témoignage",max_length=200)
    date_of_publication=models.DateTimeField("Dernière date de publication",default=timezone.now)
    details=models.TextField("Détails du témoignage")
    logo=models.ImageField("logo du groupe",upload_to="temoignage",null=True,blank=True)
    
    class Meta:
        verbose_name="Témoignage"
        verbose_name_plural="Témoignages"
    
    def __str__(self):
        return "%s %s"%(self.auteur,str(self.date_of_publication))
    
class Valeur(models.Model):
    titre=models.CharField("titre de la valeur",max_length=250)
    texte=models.TextField("Valeur")
    icon=models.CharField("Icône de la valeur ",max_length=250,default="award")
    image=models.ImageField("Image de la valeur",upload_to="valeurs",default=" ")

    def __str__(self):
        return self.titre
    
    class Meta:
        verbose_name="Valeur"
        verbose_name_plural="Valeurs"

class TypeFormulaire(models.Model):

    nom=models.CharField("type du formulaire",max_length=250)
    is_available=models.BooleanField("Le formulaire est-il disponible")
    icon=models.CharField("Icône du formulaire ",max_length=250,default="award")
    description=models.TextField("Description du formulaire")
    lien=models.CharField("Lien Formulaire",max_length=50,default="ecommerce")


    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name="Type de formulaire"
        verbose_name_plural="Type de formulaires"

