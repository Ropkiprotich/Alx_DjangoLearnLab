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
