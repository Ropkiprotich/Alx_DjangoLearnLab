# relationship_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.book_list, name='list'),
    path('details/', views.BookDetailView.as_view(), name='details'),
]
