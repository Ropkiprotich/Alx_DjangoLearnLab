from django.contrib import admin

# Register your models here.
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')  # Display the associated user and role in the admin list view
    search_fields = ('user__username', 'role')  # Add search functionality by username and role
    list_filter = ('role',)  # Add a filter by role
