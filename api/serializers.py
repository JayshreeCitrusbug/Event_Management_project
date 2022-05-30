from rest_framework import serializers
from event.models import Artist, Event, User


class EventListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ArtistListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class UserListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'