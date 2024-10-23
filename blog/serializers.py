from rest_framework import serializers
from .models import Billet

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Billet
        fields=('id','titre','slug','icon')