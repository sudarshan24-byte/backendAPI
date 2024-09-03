from rest_framework import serializers
from ..models import Post

class PostModelSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'tag', 'author')

    def get_author(self, obj):
        return obj.author.username