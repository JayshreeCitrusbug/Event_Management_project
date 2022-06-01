from email.policy import default
from rest_framework import fields, serializers
from event.models import Event
from .artist_serializer import ArtistListingSerializer



         
class EventListingSerializer(serializers.ModelSerializer):
    artist = ArtistListingSerializer(many=True, read_only=True)
    genre = serializers.RelatedField(source='Genre', read_only=True)


    class Meta:
        model = Event
        fields = ['genre','name','description','artist']

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