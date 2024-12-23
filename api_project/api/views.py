from django.shortcuts import render
# Create your views here.
from rest_framework import generics 
from .serializers import BookSerializer
from .models import Book


class BookListCreateAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    