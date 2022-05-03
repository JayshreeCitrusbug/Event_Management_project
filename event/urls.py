from django.urls import path
from . import views   
from event.views import EventListview, EventDetailView

urlpatterns = [
    path('' , views.main, name='home'),  
    path('event/' , EventListview.as_view(), name='event-list'),
    path('eventdetail/<int:pk>', EventDetailView.as_view(), name='event-detail'),
    
]