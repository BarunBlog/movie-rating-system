from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .serializers import (
    UserCreateSerializer,
)


class UserRegistrationView(generics.CreateAPIView):
    """ Api to register the user """
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "User registration successful"},
            status=status.HTTP_201_CREATED
        )
