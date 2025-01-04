from django.contrib import admin
from .models import Author, Book

# Custom filter for publication year
class PublicationYearFilter(admin.SimpleListFilter):
    title = 'publication year'  # Title in the admin interface
    parameter_name = 'publication_year'  # Query parameter name

    def lookups(self, request, model_admin):
        # Provide a list of available years as filter options
        years = Book.objects.values_list('publication_year', flat=True).distinct()
        return [(year, str(year)) for year in sorted(years)]

    def queryset(self, request, queryset):
        # Filter the queryset based on the selected year
        if self.value():
            return queryset.filter(publication_year=self.value())
        return queryset

# Admin configuration for Author model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# Admin configuration for Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_year', 'author')
    search_fields = ('title', 'author__name')
    list_filter = (PublicationYearFilter,)  # Use custom filter for publication year

