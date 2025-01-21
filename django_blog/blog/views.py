from django.shortcuts import render,redirect
# Create your views here.
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('profile')  # Redirect to profile page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Profile view
def profile(request):
    return HttpResponse("<h1>Welcome to your Profile!</h1>")


from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Profile management view
@login_required
def profile(request):
    return render(request, 'profile.html')
