from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


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
