from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

# 2. List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian
def get_librarian_for_library(library_name):
    # Retrieve the library object
    library = Library.objects.get(name=library_name)
    # Use Librarian.objects.get to retrieve the librarian associated with this library
    return Librarian.objects.get(library=library)