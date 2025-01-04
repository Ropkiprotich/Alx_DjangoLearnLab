from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Fields to display in the list view
    search_fields = ("title", "author")  # Fields to search within the admin
    list_filter = ("publication_year",) 

admin.site.register(Book, BookAdmin)


class CustomUserAdmin(UserAdmin):
    # Specify the fields to display in the admin panel
    model = CustomUser
    list_display = ('username', 'email', 'phone_number', 'date_of_birth', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'profile_picture')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'profile_picture', 'phone_number', 'date_of_birth', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

# Register the custom user model
admin.site.register(CustomUser, CustomUserAdmin)
