from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from bookshelf.models import Book
from django.contrib.auth.models import User, Permission

class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()

   

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.email})"
    
    

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)
    

class Meta:
        permissions = [
            ("can_view", "Can view book details"),
            ("can_create", "Can create new book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
