from django.urls import path
from .views import CreateMovie, ListMovie

urlpatterns = [
    path('create-movie', CreateMovie.as_view(), name="create_movie"),
    path('get-movies', ListMovie.as_view(), name="list_movie"),
]
