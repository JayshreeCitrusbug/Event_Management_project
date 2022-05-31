from django.urls import path
from .. import  views

urlpatterns = [
    path("events/", views.EventListingAPIView.as_view(), name='events'),
    path('events/<int:pk>/', views.EventDetail.as_view() , name ='event-detail'),
]