import uuid

from rest_framework import status, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from apps.users.models import User
from apps.users.serializers import UserSerializer, RegistrationSerializer
import logging


logger = logging.getLogger(__name__)


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        # serializer.is_valid(raise_exception= True)
        # serializer.save()

        if serializer.is_valid():
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "message": "User created successfully",
                "User": serializer.data}, status=status.HTTP_201_CREATED
            )
        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'me':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]

        return [permission() for permission in permission_classes]

    @action(methods=['get'], detail=False, permission_classes=[IsAuthenticated], url_path='me', url_name='me')
    def me(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
