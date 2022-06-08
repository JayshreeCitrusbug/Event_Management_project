from django.urls import path
from .. import  views

urlpatterns = [
    path("eventserializer/", views.EventAPIView.as_view(), name='eventserializer'),
    path("events/", views.EventListingAPIView.as_view(), name='events'),
    path('events/<int:pk>/', views.EventDetailAPIView.as_view() , name ='event-detail'),
    path("events/update/<int:pk>/", views.EventUpdateAPIView.as_view(), name='event-update'),
    path("events/add/", views.EventAddAPIView.as_view(), name='event-add'),
]