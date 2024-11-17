# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app import views
from .views import list_books, LibraryDetailView, register, BookDetailView
from . import views



urlpatterns = [
    path('books/', list_books, name='list_books'),  # For the list_books function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),  # For user login
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
