from django.urls import include, path
from . import event_url, artist_url, user_url

# app_name = 'user'

urlpatterns = [
    path("", include(user_url)),
    path("", include(event_url)),
    path("", include(artist_url)),
]