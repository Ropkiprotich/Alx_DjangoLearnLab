from django.urls import path
# Import Django's built-in views
from django.contrib.auth import views as auth_views 
# Import views from blog/views.py
from . import views  
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/',views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]