from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse_lazy
from django.utils import timezone

apptype=(

        ('Annuaire','Annuaire en ligne'),
        ('Ecommerce','Application Ecommerce'),
        ('Vitrine','Site Vitrine'),
        ('Blog','Blog'),
        ('Forum','Forum'),
        ('Formation','Formation en ligne'),
        ('CTR','Communication en temps réel')
    )

yesorno=(
    ('OUI','Oui'),
    ('NON','Non')
)

class Generic(models.Model):

    

    #présentation du demandeur
    username=models.CharField("Nom et prénoms du demandeur",help_text="Entrez votre nom et votre(vos) prénom(s)",max_length=250,default=" ",null=True)
    mail=models.EmailField("Email du demandeur",help_text="Entrez votre email courant",default=" ")
    numero=models.CharField("Numéros du demandeur",max_length=250,help_text="Entrez votre(vos) numéros de téléphone",default=" ",null=True)
    domaine=models.CharField("Nom de domaine de l'organisation",max_length=100,help_text="Précisez le nom du domaine que vous désirez <span class='fw-bolder'>exemple: www.yume.ci</span> <br> ou donnez juste le nom de l'application <span class='fw-bolder'>exemple: YumeStore </span>.",default=" ",null=True)
    
    #présentation du projet
    type=models.CharField("Type d'application",choices=apptype,max_length=250,help_text="Quel type d'application désirez vous Choisissez parmi les éléments proposez",default="Vitrine",null=True)
    produits=models.TextField("Produits et/ou services",help_text="Indiquez les produits et/ou les services vendus (marques, gammes et lignes de produits...)",default=" ",null=True)
    objectifs=models.TextField("Objectifs attendus",help_text="Détaillez le ou les objectifs attendus avec cette nouvelle application. Vous pouvez découper vous objectifs en 2 parties : quantitatifs et qualitatifs.",default="",null=True)
    objectifs_pdf=models.FileField("Objectifs au format pdf",help_text="Si vos objectifs sont au format pdf alors laissez téléversé le document pdf contenant vos objectifs bien détaillés",upload_to="formulaire/visualid",validators=[FileExtensionValidator('pdf',message="Le fichier doit être au format pdf")],null=True,blank=True)
    clientele=models.TextField("Profil de la clientèle",help_text="Décrivez le profil des clients que vous espérez obtenir pour votre entreprise ? Décrivez au maximum vos cibles, leurs âges, leurs habitudes...",default="",null=True)
    clientele_pdf=models.FileField("Profil de la clientèle au format pdf",help_text="Décrivez le profil des clients que vous espérez obtenir pour votre entreprise ? Décrivez au maximum vos cibles, leurs âges, leurs habitudes...",default="",null=True)
    description=models.TextField("Description de l'application",help_text="Donnez nous une description du site que vous aimeriez avoir en précisant (couleur, design et autres)",default="",null=True)
    description_pdf=models.FileField("Description détaillée du site web",help_text="Donnez nous une description du site que vous aimeriez avoir en précisant (couleur, design et autres)",default="",null=True)
    date_butoire=models.DateField("Date de lancement",help_text="Avez-vous une date butoire pour le lancement du projet ?",null=True)
    
    #graphisme
    wireframe_file=models.FileField("Structure du site Web au format image ou pdf",help_text="Avez-vous une structure définie du site e-commerce au format pdf ou image (jpg,png,et jpeg)?",null=True)  
    visualid=models.FileField("Identité visuelle",help_text="Si vous avez une identité visuelle téléverser le document au format pdf sinon laissez le champ vide",upload_to="formulaire/visualid/%Y",validators=[FileExtensionValidator('pdf',message="Le fichier doit être au format pdf")],null=True,blank=True)
    reference=models.CharField("Application de référence",help_text="Avez vous des sites de référence ( des sites que vous appréciez)? énumerez les",max_length=250,default="",null=True)
    logo=models.FileField("Logo de votre organisation",help_text="Téléversez votre logo si vous en avez un",upload_to="formulaires/logo/%Y",validators=[FileExtensionValidator(['jpg','svg','png','jpeg'],message="Le fichier doit être au format svg,png,jpeg ou jpg")],null=True,blank=True)
    couleurs=models.TextField("Couleur(s)",default="Mes couleurs sont: ",help_text="Définissez vos couleurs et vos préférences graphiques",null=True)

    #Entretien et Après projet
    texteseo=models.CharField("Référencement SEO",max_length=10,choices=yesorno,help_text="Voulez-vous que nous revoyons vos textes pour les adapter aux référencement web (ou voulez vous que nous rédigeons votre contenu textuel)? ",default=True)
    entretien=models.CharField("Entretien",max_length=10,choices=yesorno,help_text="Voulez vous que nous nous chargeons de l'entretien du site après sa création ? ",default=True)
    promotion=models.CharField("Promotion",max_length=10,choices=yesorno,help_text="Voulez-vous que nous fassions la promotion de votre futur site web?",default=True)
    keywords=models.TextField("Mots clés",help_text="Précisez les mots clés que vous désirez.",default="",null=True)
    divers=models.TextField("Ajouts",help_text="Dites ce que vous désirez de plus pour votre site que nous avons peut-être omis .",default="",null=True)
    slug=models.SlugField("Slug de l'utilisateur",default=" ")

class Vitrine(Generic):
    pass

class Ecommerce(Generic):
    fiche=models.TextField(" Fiche produit",help_text="Définissez ce que comportera chaque fiche produit (comment sera présenté un produit)?",default="",null=True)
    paiement=models.TextField("Moyens de paiement",help_text="Quelles sont les solutions de paiement à intégrer sur le site?(paypal, mtn money, moov money, orange money...)",default="",null=True)
    appdedie=models.CharField("Voulez-vous une application mobile dédié(ou une application web) pour votre application d'ecommerce?",help_text="Voulez-vous une application mobile dédié(ou une application web) pour votre application d'ecommerce?",default=True,max_length=250,choices=yesorno)
    
class Annuaire(Generic):
    pass

class Blog(Generic):
    commentaire=models.CharField("Voulez-vous que votre blog possède un suivi des commentaires?",help_text="Voulez-vous un suivi des commentaires du blog?",default=True,max_length=250,choices=yesorno)

class Forum(Generic):
    pass

class CTR(Generic):
    pass