
from formulaire.models import Blog, Ecommerce, Vitrine
from .models import Client
from django.forms import CharField, CheckboxInput,DateInput, ClearableFileInput, FileField, ImageField, ModelForm,EmailInput, PasswordInput, SelectMultiple, TextInput, Textarea,Select,FileInput, URLInput
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator,FileExtensionValidator
from django.utils.translation import gettext_lazy as _
import re
from django.utils import timezone



def validate_password(value):
    level1=re.compile('.*[a-z]+.*')
    level2=re.compile('.*[A-Z]+.*')
    level3=re.compile('.*[0-9]+.*')

    if level1.match(value)== None:
        raise ValidationError(
            _('Le mot de passe doit contenir des lettres miniscules'),
            params={'value':value}
        )
    elif level2.match(value)== None:
        raise ValidationError(
            _('Le mot de passe doit contenir des lettres majuscules'),
            params={'value':value}
        )
    elif level3.match(value)== None:
        raise ValidationError(
            _('Le mot de passe doit contenir au moins 1 chiffre pour plus de sécurité'),
            params={'value':value}
        )

fonction=(
        ('Visiteur','Visiteur'),
        ('Membre','Membre'),
        ('Prédicateur','Prédicateur'),
        ('Coach','Coach ou formateur'),
        ('Blogueur','Blogueur')
    ) 


class InscriptionForm(forms.Form):
    username=forms.CharField(label='Entrer votre nom en entier',max_length=30,widget=TextInput(attrs={
            'placeholder':"Entrer votre nom en entier",
            'class':'form-control border border-dark border-1 my-1',
           
            'autocomplete':'username',
        }))
    number=forms.CharField(label='Numéro de téléphone',min_length=8,widget=TextInput(attrs={
            'placeholder':"Entrez votre numéro de téléphone",
            'class':'form-control border border-dark border-1 my-1',
            'autocomplete':'tel',
        }))
    email=forms.CharField(label='email',validators=[EmailValidator("Enter une email valide. ex:john@doe.com")],widget=EmailInput(attrs={
            'placeholder':"Entrez votre e-mail",
            'class':'form-control border border-dark border-1 my-1',
            'autocomplete':'email',
        }))
    password=forms.CharField(min_length=6,max_length=40,validators=[validate_password],widget=PasswordInput(attrs={
            'placeholder':"Entrez votre mot de passe",
            'class':'form-control border border-dark border-1 my-1',
            'autocomplete':'false'
        }))
    password_confirm=forms.CharField(max_length=40,widget=PasswordInput(attrs={
            'placeholder':"Entrez votre mot de passe à nouveau",
            'class':'form-control border border-dark border-1 my-1',
            'autocomplete':False
        }))
    referenced=forms.BooleanField(label="Voulez vous êtes référencé",widget=CheckboxInput(attrs={
        'class':'custom-control-input',
        'checked':False,
        
    }))

class ConnexionForm(forms.Form):
    email=forms.EmailField(label='email',required=True,max_length=30,widget=TextInput(attrs={
            'placeholder':"Entrez votre email",
            'class':'form-control border border-dark border-1'
        }))
    password=forms.CharField(min_length=6,required=True,max_length=40,widget=PasswordInput(attrs={
            'placeholder':"Entrez votre mot de passe",
            'class':'form-control border border-dark border-1',
            'autocomplete':'password',
        }))

class CommentForm(forms.Form):
    message=forms.CharField(label='Laissez un commentaire',widget=TextInput(attrs={
            'placeholder':"Laissez un commentaire",
            'class':'form-control border border-dark border-1 m-1 rounded-pill',            
        }))

class ForumForm(forms.Form):
    titre=forms.CharField(label="Titre de la discussion",required=True,widget=TextInput(attrs={
        'placeholder':'Titre de la discussion',
        'class':'form-control border border-dark border-1 m-1',
    }))
    contenu=forms.CharField(label="Le contenu de votre discussion",required=True,widget=Textarea(attrs={
        'placeholder':'Le contenu de votre discussion',
        'class':'form-control border border-dark border-1 m-1',
        'cols':'30',
        'rows':'10'
    }))
    image=forms.ImageField(required=False,widget=ClearableFileInput(attrs={
        'placeholder':"Ajouter une image",
        'class':'form-control border border-dark border-1 m-1',
    }))
class DiscussionForm(forms.Form):
    contenu=forms.CharField(label="Le contenu de votre discussion",required=True,widget=Textarea(attrs={
        'placeholder':'Le contenu de votre discussion',
        'class':'form-control border border-dark border-1 m-1',
        'cols':'30',
        'rows':'10'
    }))
    image=forms.ImageField(required=False,widget=ClearableFileInput(attrs={
        'placeholder':"Ajouter une image",
        'class':'form-control border border-dark border-1 m-1',
    }))

class UpdatePofileForm(ModelForm):
    photo=ImageField(required=False,validators=[FileExtensionValidator(['jpeg','jpg','png'],"Le fichier n'est pas au bon format. entrez un fichier au format jpeg, png ou jpg")],widget=FileInput(attrs={
                'placeholder':'Entrez une photo de profil',
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'off',
            }))

    class Meta:
        model=Client
        fields=('nom_du_profil','email','numero','about','siteweb','photo','activite','first_name','last_name','adresse')
        widgets={
            'nom_du_profil':TextInput(attrs={
                'placeholder':"Entrer votre nom en entier",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'username',
            }),
            'first_name':TextInput(attrs={
                'placeholder':"Entrez votre nom de famille",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'username',
            }),
            'last_name':TextInput(attrs={
                'placeholder':"Entrez vos prénoms",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'username',
            }),
            'email':EmailInput(attrs={
                'placeholder':"Entrer votre email",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'email',
            }),
            'numero':TextInput(attrs={ 
                'placeholder':'Entrez votre numéro de téléphone',
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'number',
                
            }),
            'about':Textarea(attrs={
                'placeholder':'Entrez une description détaillé de votre organisation ou de votre activité',
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'off',
            }),
            'siteweb':URLInput(attrs={
                'placeholder':"Entrez l'url de votre Site Web",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'url',
            }),
            'activite':SelectMultiple(attrs={
                'placeholder':"Choisissez les Activités que vous faites",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'off',
            }),
            'adresse':TextInput(attrs={
                'placeholder':"Donnez l'adresse de votre organisation",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'url',
            }),
            
        }
        help_texts={
            'nom_du_profil':_('Votre nom de profil est le nom qui apparaîtra sur les moteurs de recherche'),
            'email':_("Entrez un mail valide que vous utilisez couramment"),
            'numero':_("Entrez un numéro valide en incluant le préfixe sans symbole +"),
            'about':_("Entrez une description détaillée de votre organisation ou de votre activité"),
            'siteweb':_("Entrez une URL valide de votre site web"),
            'photo':_("Entrez une photo au format jpeg,jpg ou png"),
            'activite':_("Choisissez une ou plusieurs activités. Pour choisir plusieurs activités maintenez la touche ctrl de votre clavier et choisissez"),
            'adresse':_("Donnez votre  adresse pour que les clients sache où vous localisez")
        }

class EcommerceCreateForm(ModelForm):
    #informations générales
    username=CharField(required=False, widget=TextInput(attrs={
                'placeholder':"Entrez votre nom en entier",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'username',
            }))
    mail=CharField(required=False, widget=EmailInput(attrs={
                'placeholder':"Entrez votre email",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'email',
            }))
    domaine=CharField(required=False, widget=TextInput(attrs={
                'placeholder':"Nom de domaine (eg: www.yume.ci)",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    numero=CharField(required=False, widget=TextInput(attrs={
                'placeholder':"Numéro(s) de téléphone",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    #détails sur le projet
    produits=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Enumérez vos produit et services",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    produits_pdf=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Enumérez vos produits et/ou services",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    objectifs=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Détaillez les objectifs de votre projet",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    objectifs_pdf=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Détaillez les objectifs de votre projet",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    clientele=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Profile de la clientèle",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':6
            }))
    clientele_pdf=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Profil de la clientèle en version pdf",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    keywords=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Donnez les mots clés qui seront utilisés pour le référencement organique",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    description=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Description",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    description_pdf=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Description",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    wireframe_file=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Wireframe",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    reference=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Application de référence",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    visualid=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Joindre une identité visuelle",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    divers=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Divers",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    couleurs=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Vous pouvez utilisez le bouton de choix de couleurs ci-dessous",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':4
            }))
    paiement=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Moyens de paiement in-app",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':4
            }))
    fiche=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Description de la fiche produit",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    logo=CharField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Joindre un logo",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    date_butoire=CharField(required=False, widget=DateInput(attrs={
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'type':'date',
                'required':'false',
            }))
    class Meta:
        model=Ecommerce
        
        fields=('username','mail','domaine','numero','type','produits','objectifs','objectifs_pdf','clientele','clientele_pdf','texteseo','entretien','promotion','keywords','date_butoire','description','description_pdf','wireframe_file','reference','visualid','divers','logo','couleurs','fiche','appdedie','paiement','slug')
        widgets={
             'texteseo':Select(attrs={
                'placeholder':"Voulez-vous que nous revoyons vos textes pour les adapter au référencement",
                'class':' form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }),
             'promotion':Select(attrs={
                'placeholder':"Promotion de l'application",
                'class':' form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }),
            'appdedie':Select(attrs={
                'placeholder':"Application dédié",
                'class':' form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }),
            'entretien':Select(attrs={
                'placeholder':"Entretien de l'application après création",
                'class':' form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }),
            'type':Select(attrs={
                'placeholder':"Type de l'application recherché",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }),
            'slug':TextInput(attrs={
                'placeholder':"Type de l'application recherché",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'type':"hidden"
            }),
    
        }
       
class VitrineCreateForm(ModelForm):
    #informations générales
    username=CharField(required=False, widget=TextInput(attrs={
                'placeholder':"Entrez votre nom en entier",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'username',
            }))
    mail=CharField(required=False, widget=EmailInput(attrs={
                'placeholder':"Entrez votre email",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'email',
            }))
    domaine=CharField(required=False, widget=TextInput(attrs={
                'placeholder':"Nom de domaine (eg: www.yume.ci)",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    numero=CharField(required=False, widget=TextInput(attrs={
                'placeholder':"Numéro(s) de téléphone",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    #détails sur le projet
    produits=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Enumérez vos produit et services",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    produits_pdf=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Enumérez vos produits et/ou services",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    objectifs=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Détaillez les objectifs de votre projet",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    objectifs_pdf=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Détaillez les objectifs de votre projet",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    clientele=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Profile de la clientèle",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':6
            }))
    clientele_pdf=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Profil de la clientèle en version pdf",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    keywords=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Donnez les mots clés qui seront utilisés pour le référencement organique",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    description=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Description",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    description_pdf=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Description",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    wireframe_file=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Wireframe",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    reference=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Application de référence",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    visualid=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Joindre une identité visuelle",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    divers=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Divers",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    couleurs=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Vous pouvez utilisez le bouton de choix de couleurs ci-dessous",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':4
            }))
    logo=CharField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Joindre un logo",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    date_butoire=CharField(required=False, widget=DateInput(attrs={
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'type':'date',
                'required':'false',
            }))
    class Meta:
        model=Vitrine
        
        fields=('username','mail','domaine','numero','type','produits','objectifs','objectifs_pdf','clientele','clientele_pdf','texteseo','entretien','promotion','keywords','date_butoire','description','description_pdf','wireframe_file','reference','visualid','divers','logo','couleurs','slug')
        widgets={
             'texteseo':Select(attrs={
                'placeholder':"Voulez-vous que nous revoyons vos textes pour les adapter au référencement",
                'class':' form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }),
             'promotion':Select(attrs={
                'placeholder':"Promotion de l'application",
                'class':' form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }),
            'entretien':Select(attrs={
                'placeholder':"Entretien de l'application après création",
                'class':' form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }),
            'type':Select(attrs={
                'placeholder':"Type de l'application recherché",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }),
            'slug':TextInput(attrs={
                'placeholder':"Type de l'application recherché",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'type':"hidden"
            }),
    
        }

class BlogCreateForm(ModelForm):
    #informations générales
    username=CharField(required=False, widget=TextInput(attrs={
                'placeholder':"Entrez votre nom en entier",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'username',
            }))
    mail=CharField(required=False, widget=EmailInput(attrs={
                'placeholder':"Entrez votre email",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':'email',
            }))
    domaine=CharField(required=False, widget=TextInput(attrs={
                'placeholder':"Nom de domaine (eg: www.yume.ci)",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    numero=CharField(required=False, widget=TextInput(attrs={
                'placeholder':"Numéro(s) de téléphone",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    #détails sur le projet
    produits=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Enumérez vos produit et services",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    produits_pdf=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Enumérez vos produits et/ou services",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    objectifs=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Détaillez les objectifs de votre projet",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    objectifs_pdf=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Détaillez les objectifs de votre projet",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    clientele=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Profile de la clientèle",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':6
            }))
    clientele_pdf=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Profil de la clientèle en version pdf",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    keywords=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Donnez les mots clés qui seront utilisés pour le référencement organique",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    description=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Description",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    description_pdf=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Description",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    wireframe_file=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Wireframe",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    reference=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Application de référence",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    visualid=FileField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Joindre une identité visuelle",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    divers=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Divers",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':5
            }))
    couleurs=CharField(required=False, widget=Textarea(attrs={
                'placeholder':"Vous pouvez utilisez le bouton de choix de couleurs ci-dessous",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'rows':4
            }))
    logo=CharField(required=False, widget=ClearableFileInput(attrs={
                'placeholder':"Joindre un logo",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }))
    date_butoire=CharField(required=False, widget=DateInput(attrs={
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'type':'date',
                'required':'false',
            }))
    class Meta:
        model=Blog
        
        fields=('username','mail','domaine','numero','type','produits','objectifs','objectifs_pdf','clientele','clientele_pdf','texteseo','entretien','promotion','keywords','date_butoire','description','description_pdf','wireframe_file','reference','visualid','divers','logo','couleurs','slug','commentaire')
        widgets={
             'texteseo':Select(attrs={
                'placeholder':"Voulez-vous que nous revoyons vos textes pour les adapter au référencement",
                'class':' form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }),
             'promotion':Select(attrs={
                'placeholder':"Promotion de l'application",
                'class':' form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }),
            'entretien':Select(attrs={
                'placeholder':"Entretien de l'application après création",
                'class':' form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }),
            'commentaire':Select(attrs={
                'placeholder':"Voulez vous une section dédiée au commentaire sur le blog",
                'class':' form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }),
            'type':Select(attrs={
                'placeholder':"Type de l'application recherché",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
            }),
            'slug':TextInput(attrs={
                'placeholder':"Type de l'application recherché",
                'class':'form-control border border-dark border-1 my-1',
                'autocomplete':False,
                'type':"hidden"
            }),
    
        }
