from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

# This returns currently active user model
User = get_user_model()


class Movie(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    release_date = models.DateField()

    def __str__(self):
        return self.name


class MovieRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]
    )

    class Meta:
        unique_together = (('user', 'movie'),)

    def __str__(self):
        return self.movie.name


