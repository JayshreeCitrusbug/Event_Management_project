from django.urls import include, path
from . import event_url, artist_url, user_url, genre_url, eventbook_url

# app_name = 'user'

urlpatterns = [
    path("", include(user_url)),
    path("", include(event_url)),
    path("", include(artist_url)),
    path("", include(genre_url)),
    path("",include(eventbook_url))
]