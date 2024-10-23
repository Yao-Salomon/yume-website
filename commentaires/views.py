from commentaires.models import ReponsesCommentaire
from commentaires.models import CommentaireBlog
from commentaires.serializers import CommentaireBlogSerializer, ReponseBlogSerializer
from rest_framework import viewsets

#vue pour le frameworks djangorest

class CommentaireBlogViewset(viewsets.ReadOnlyModelViewSet):
    
    serializer_class=CommentaireBlogSerializer

    def get_queryset(self):

        queryset=CommentaireBlog.managed_objects.all()
        id=self.request.GET.get('id')

        if id is not None:
            queryset=queryset.filter(id=id)

        return queryset

class ReponseCommentaireBlogViewset(viewsets.ReadOnlyModelViewSet):
    
    serializer_class=ReponseBlogSerializer

    def get_queryset(self):

        queryset=ReponsesCommentaire.managed_objects.all()
        id=self.request.GET.get('id')

        if id is not None:
            queryset=queryset.filter(id=id)

        return queryset