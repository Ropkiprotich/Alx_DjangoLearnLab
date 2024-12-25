from rest_framework import serializers
from  .models import Book
from .models import Post

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '_all_'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']