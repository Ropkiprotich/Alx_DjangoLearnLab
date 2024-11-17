from django.shortcuts import render
from django.views.generic.detail import DetailView


# Create your views here.



from .models import Book
from .models import Book
from .models import Library

def list_books(request):
    return render(request, "relationship_app/list_books.html")

def book_list(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'book_list': books}  # Create a context dictionary with book list
    return render(request, 'books/book_list.html', context)

def library_detail(request):
    # Sample context data, replace with your actual logic
    context = {
        "library": {
            "name": "Central Library",
            "location": "Downtown",
            "books": 1200,
        }
    }
    return render(request, "relationship_app/library_detail.html", context)

class BookDetailView(DetailView):
    """A class-based view for displaying details of a specific book."""
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the book."""
        context = super().get_context_data(**kwargs)  # Get default context data
        book = self.get_object()  # Retrieve the current book instance
        context['average_rating'] = book.get_average_rating() 
