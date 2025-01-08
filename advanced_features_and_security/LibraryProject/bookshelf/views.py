from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import ExampleForm

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView
from .models import Book

class BookDetailView(PermissionRequiredMixin, DetailView):
    model = Book
    permission_required = 'bookshelf.can_view'
    template_name = 'book_detail.html'
    raise_exception = True

    bookshelf__list = 'book_list'
def index(request):
     return HttpResponse('Welcome to my bookshelf.')

def example_view(request):
    form = ExampleForm()
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            print(form.cleaned_data)
    return render(request, 'example_template.html', {'form': form})