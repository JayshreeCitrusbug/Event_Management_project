from django.urls import path
from .. import views

urlpatterns = [
    path('genres/', views.GenreListingAPIView.as_view(), name='genre-list'),
]
