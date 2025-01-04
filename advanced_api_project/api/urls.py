from django.urls import path
from . import views 

urlpatterns = [
    # Example API endpoint for listing authors
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    # Example API endpoint for listing books
    path('books/', views.BookListView.as_view(), name='book-list'),
]