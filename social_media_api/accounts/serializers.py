from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import UserSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    bio = serializers.CharField(allow_blank=True, required=False)

    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({'token': token.key, 'user_id': user.pk, 'username': user.username})

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
