from django.views.generic.detail import DetailView

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Book
from .models import Library


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect("home")  # Redirect to a homepage or other view
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})

def list_books(request):
    # Add your logic for fetching and rendering books
    books = []  # Replace with actual query, e.g., Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


class BookDetailView(DetailView):
    """A class-based view for displaying details of a specific book."""
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the book."""
        context = super().get_context_data(**kwargs)  # Get default context data
        book = self.get_object()  # Retrieve the current book instance
        context['average_rating'] = book.get_average_rating() 


from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('relationship_app.view_admin', raise_exception=True)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
