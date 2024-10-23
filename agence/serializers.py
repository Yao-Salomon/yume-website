from rest_framework import serializers

from blog.models import Billet
from .models import Fonctionalite, Produit

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produit
        fields=('id','nom','subtitle','price','icon')

class FonctionaliteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fonctionalite
        fields=('id','nom','icon')
