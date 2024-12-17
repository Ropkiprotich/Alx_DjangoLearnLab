from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = 'authors')
    def __str__(self):
        return self.title
#manytomany relationshis

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name ='books')
    def __str__(self):
        return self.name
# one to one relationship

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    
class Meta:
        permissions = [
            ("view_admin", "Can view admin dashboard"),
            ("manage_librarians", "Can manage librarians"),
            ("access_member_content", "Can access member content"),
        ]

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Automatically create UserProfile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="DOB")
    profile_photo = models.ImageField(upload_to='profile_photos/')
    # ... additional fields as needed ...