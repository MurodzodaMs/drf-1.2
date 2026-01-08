from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .models import *
from .serializers import *


class RegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_api_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Fields are required'},
                status=status.HTTP_400_BAD_REQUEST 
            )
        user = authenticate(request, 
            username=username, 
            password=password, 
            email=email
        )
        if user:
            login(request, user)
            return Response('User logged in', status=status.HTTP_200_OK)
        return Response('Invalid credentials', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def logout_api_view(request):
    try:
        logout(request)
        return Response('you are logged out', status=status.HTTP_200_OK)
    except Exception as err:
        return Response(f'{err}', status=status.HTTP_400_BAD_REQUEST)