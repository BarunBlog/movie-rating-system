from rest_framework import serializers
from .models import Movie, MovieRating
from django.db.models import Avg


class CreateMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ["name", "genre", "rating", "release_date"]


class GetMovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "name", "genre", "rating", "release_date", "average_rating"]

    def get_average_rating(self, obj):
        average_rating = MovieRating.objects.filter(movie_id=obj.id).aggregate(Avg('rating'))['rating__avg']
        formatted_average_rating = round(average_rating, 2) if average_rating is not None else 0.00
        return formatted_average_rating


class RateMovieSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField(required=True)
    rating = serializers.FloatField(min_value=1, max_value=5)


class SearchMoviesSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=200,
        error_messages={'required': 'The parameter is required in the query params.'}
    )

