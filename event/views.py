from re import template
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from event.models import Event, Artist, EventBook, Genre

#Main page
def main(request):
    return render(request, 'event/home.html' , {})

class EventListview(ListView):
    model = Event
    template_name = 'event/event_list.html'

class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event_detail.html'