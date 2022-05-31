from django.urls import path
from .. import  views

urlpatterns = [
    path("artists/", views.ArtistListingAPIView.as_view(), name='artists'),
]