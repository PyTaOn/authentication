from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializer import CustomUserSerializer

from rest_framework import viewsets
from rest_framework.response import Response


class CustomUserViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        customUser_data = request.data
        new_customUser = CustomUser(email=customUser_data["email"], password=customUser_data["password"])

        serializer = CustomUserSerializer(data={"email":new_customUser.email, "password":new_customUser.password})

        if serializer.is_valid():
            new_customUser.save()
            return Response(serializer.data, status=201)
        return Response('field must be filled.', status=422)
