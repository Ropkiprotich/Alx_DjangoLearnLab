from django.urls import path
from .views import UserRegistrationView, CustomObtainAuthToken, UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', CustomObtainAuthToken.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
