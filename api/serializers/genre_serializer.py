from rest_framework import fields, serializers
from rest_framework.response import Response
from event.models import Genre, Event
from api.serializers.event_serializer import EventGenre

class GenreListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','name']
  

class GenreListUseInEventFetch(serializers.ModelSerializer):
       class Meta:
        model = Genre
        fields = ['name']


class GenreAddSerializer(serializers.ModelSerializer):
    """
    Genre Add serializer
    """    
    class Meta:
        model = Genre
        fields = "__all__"


class GenreEventSerializer(serializers.Serializer):
    """
    Event by genre
    """
    events = EventGenre(many=True)
    genre = GenreListUseInEventFetch()
    
    class Meta:
        fields = ["genre", "events"]
    
        

