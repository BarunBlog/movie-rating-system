from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    release_date = models.DateField()

    def __str__(self):
        return self.name

