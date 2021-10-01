from pyexpat.errors import messages

from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from apps.users.models import User
from apps.users.serializers import AuthRegisterSerializer, UserSerializer
from apps.users.services import register_user
import logging
logger = logging.getLogger(__name__)


class AuthViewSet(ViewSet):

    @action(methods=['post'], detail=False, permission_classes=[], url_path='register', url_name='register')
    def register(self, request):
        serializer = AuthRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = register_user(request.data)
            serializer = UserSerializer(user)
            logger.info(f"User Registered : {user.role} (PK: {user.pk}) {user}")
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, permission_classes=[], url_path='login', url_name='login')
    def login(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'me':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]

        return [permission() for permission in permission_classes]
