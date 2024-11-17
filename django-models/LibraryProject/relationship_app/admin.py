from django.contrib import admin

# Register your models here.
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')  # Display the associated user and role in the admin list view
    search_fields = ('user__username', 'role')  # Add search functionality by username and role
    list_filter = ('role',)  # Add a filter by role

from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import UserProfile

# Assign 'view_admin' permission to a user
user = User.objects.get(username='admin_user')
content_type = ContentType.objects.get_for_model(UserProfile)
permission = Permission.objects.get(codename='view_admin', content_type=content_type)
user.user_permissions.add(permission)
