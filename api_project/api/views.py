from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .serializers import BookSerializers
from .models import Book


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers