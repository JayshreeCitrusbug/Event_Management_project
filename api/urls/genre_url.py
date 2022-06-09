from django.urls import path
from .. import views

urlpatterns = [
    path('genres/', views.GenreListingAPIView.as_view(), name='genre-list'),
    path('genres/add/', views.GenreAddAPIView.as_view(), name='genre-add'),
    path('genres/update/<int:pk>/', views.GenreUpdateAPIView.as_view(), name='genre-update'),
    path('genre/eventdata/', views.GenreEventAPIView.as_view(), name='genre-event'),
]
