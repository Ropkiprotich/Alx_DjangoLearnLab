
from rest_framework.generics import ListAPIView
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# View for listing all authors
class AuthorListView(ListAPIView):
    queryset = Author.objects.all()  # Query all authors
    serializer_class = AuthorSerializer  # Use AuthorSerializer for serialization

# View for listing all books
class BookListView(ListAPIView):
    queryset = Book.objects.all()  # Query all books
    serializer_class = BookSerializer  # Use BookSerializer for serialization
