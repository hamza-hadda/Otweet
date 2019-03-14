from .models import Post, Category
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    #snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    class Meta:
        model = Post
        fields = ('url', 'content')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'title', 'description')