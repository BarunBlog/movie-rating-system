from rest_framework import serializers
from .models import Movie, MovieRating


class CreateMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ["name", "genre", "rating", "release_date"]


class GetMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ["id", "name", "genre", "rating", "release_date"]


class RateMovieSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField(required=True)
    rating = serializers.FloatField(min_value=1, max_value=5)

