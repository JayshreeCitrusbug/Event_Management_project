from django.urls import path
from . import views
from api.views import EventGet, ArtistGet,UserGet

urlpatterns =[
    path('getevent/', views.EventGet.as_view(), name='getevent'),
    path('getartist/', views.ArtistGet.as_view(), name='getartist'),
    path('getuser/', views.UserGet.as_view(), name='getuser'),

]