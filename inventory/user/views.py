from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data
    if User.objects.filter(username=data['username']).exists():
        return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(
        username=data['username'],
        email=data.get('email', ''),
        password=make_password(data['password'])  # Hash the password
    )

    refresh = RefreshToken.for_user(user)
    logger.info(f"New user registered: {user.username}")
    
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'username': user.username
    }, status=status.HTTP_201_CREATED)
