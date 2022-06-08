from django.urls import path
from .. import  views

urlpatterns = [
    path("artists/", views.ArtistListingAPIView.as_view(), name='artists'),
    path('artists/<int:pk>/', views.ArtistDetailAPIView.as_view(), name='artist-detail'),
    path('artists/update/<int:pk>/', views.ArtistUpdateAPIView.as_view(), name='artist-update'),
    path("artists/add/", views.ArtistAddAPIView.as_view(), name='artist-add'),
    path("artists/eventdata/", views.ArtistEventListAPIView.as_view(), name='artist-event'),
]