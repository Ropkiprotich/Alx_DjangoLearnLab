from django.contrib import admin

# Register your models here.
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Fields to display in the list view
    search_fields = ("title", "author")  # Fields to search within the admin
    list_filter = ("publication_year",) 

admin.site.register(Book, BookAdmin)