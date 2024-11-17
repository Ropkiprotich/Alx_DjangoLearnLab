# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from .views import register
urlpatterns = [
    path('books/', list_books, name='list_books'),  # For the list_books function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),  # For user registration
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),  # For user login
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
]
