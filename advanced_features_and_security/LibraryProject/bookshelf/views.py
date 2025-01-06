from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView
from .models import Book

class BookDetailView(PermissionRequiredMixin, DetailView):
    model = Book
    permission_required = 'bookshelf.can_view'
    template_name = 'book_detail.html'
    raise_exception = True
def index(request):
     return HttpResponse('Welcome to my bookshelf.')