# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.viewsets import ViewSet
#
# from apps.users.serializers import AuthRegisterSerializer, UserSerializer
# from apps.users.services import register_user
#
#
# class AuthViewSet(ViewSet):
#
#     def register(self, request):
#         serializer = AuthRegisterSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             user = register_user(request.data)
#             serializer = UserSerializer(user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
