from django.urls import path
from .. import  views

urlpatterns = [
    path("eventbook/", views.EventBookListingAPIView.as_view(), name="event-book"),
    path("booking/",views.EventBookAddAPIView.as_view(), name='booking'),
]