from rest_framework import generics
from .serializers import CreateMovieSerializer
from rest_framework.permissions import IsAuthenticated


class CreateMovie(generics.CreateAPIView):
    """ Api to create a movie """
    serializer_class = CreateMovieSerializer
    permission_classes = [IsAuthenticated]
