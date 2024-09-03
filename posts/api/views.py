from rest_framework import viewsets, permissions
from ..models import Post
from .serializers import PostModelSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)