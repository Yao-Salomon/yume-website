from django.shortcuts import render
from commentaires.models import CommentaireBlog
from rest_framework import serializers


#vue pour le frameworks djangorest

class CommentaireBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentaireBlog
        fields=('id','contenu','date','user','bille')

class ReponseBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentaireBlog
        fields=('id','contenu','date','user','bille')
