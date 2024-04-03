from rest_framework import generics
from .serializers import (
    CreateMovieSerializer,
    GetMovieSerializer
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
    serializer_class = GetMovieSerializer


class DetailMovie(generics.RetrieveAPIView):
    """ Api to get detail of the movie """
    serializer_class = GetMovieSerializer

    def get_queryset(self):
        return Movie.objects.filter(pk=self.kwargs['pk'])
