from django.urls import path
from .views import CreateMovie

urlpatterns = [
    path('', CreateMovie.as_view(), name="create_movie"),
]
