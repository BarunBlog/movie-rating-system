from rest_framework import generics, status
from .serializers import (
    CreateMovieSerializer,
    GetMovieSerializer,
    RateMovieSerializer,
    SearchMoviesSerializer
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Movie, MovieRating
from django.db import IntegrityError


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


class RateMovie(APIView):
    """ Api to rate a movie """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RateMovieSerializer(data=request.data)
        if serializer.is_valid():

            movie_id = request.data["movie_id"]
            rating = request.data["rating"]

            # Get the movie from the database ---------------------------------------------------------------
            try:
                movie = Movie.objects.get(id=movie_id)
            except Movie.DoesNotExist:
                return Response(
                    {"message": "Movie not found with the given id"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Save the rating to the database ---------------------------------------------------------------
            try:
                MovieRating.objects.create(user=request.user, movie=movie, rating=rating)
            except IntegrityError as e:
                print(e, flush=True)
                return Response(
                    {"message": "You have already added rating for this movie"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response({"message": "Movie rating saved successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchMovies(APIView):
    """ Api to search a movie """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = SearchMoviesSerializer(data=request.query_params)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            movies = Movie.objects.filter(name__icontains=name)
            serializer = GetMovieSerializer(movies, many=True)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
