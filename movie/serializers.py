from rest_framework import serializers
from .models import Movie


class CreateMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ["name", "genre", "rating", "release_date"]
