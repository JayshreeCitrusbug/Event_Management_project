from rest_framework import fields, serializers
from event.models import Event
from .artist_serializer import ArtistListingSerializer
from .genre_serializer import GenreListingSerializer

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name']
         
class EventListingSerializer(serializers.ModelSerializer):
    artist = ArtistListingSerializer(many=True, read_only=True)
    genre = GenreListingSerializer(read_only=True)
    
    class Meta:
        model = Event
        fields = ['name','description','eventDate','lastDateBook','seatAvailable','price','genre','artist']

class EventAddSerializer(serializers.ModelSerializer):
    """
    Event Add serializer
    """
    name = serializers.CharField(required=True)
    eventDate = serializers.DateTimeField(required=True)
    lastDateBook = serializers.DateTimeField(required=True)
    seatAvailable = serializers.IntegerField(required=True)
    price = serializers.IntegerField(required=True)
    description = serializers.CharField(required=True)
    active = serializers.BooleanField(read_only=True,default=True)

    class Meta:
        model = Event
        fields = '__all__'


# class EventUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         exclude = ['active']