from rest_framework import generics
from .serializers import (
    CreateMovieSerializer,
    ListMovieSerializer
)
from rest_framework.permissions import IsAuthenticated
from .models import Movie


class CreateMovie(generics.ListCreateAPIView):
    """ Api to create a movie """
    serializer_class = CreateMovieSerializer
    permission_classes = [IsAuthenticated]


class ListMovie(generics.ListAPIView):
    """ Api to get movie list """
    queryset = Movie.objects.all()
    serializer_class = ListMovieSerializer
