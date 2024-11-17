# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register

urlpatterns = [
    path('books/', list_books, name='list_books'),  # For the list_books function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
]
