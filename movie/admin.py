from django.contrib import admin
from .models import Movie, MovieRating


class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "genre", "rating", "release_date"]


class MovieRatingAdmin(admin.ModelAdmin):
    list_display = ["id", "rating", "movie", "user"]


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieRating, MovieRatingAdmin)
