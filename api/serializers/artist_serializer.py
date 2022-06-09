from rest_framework import fields, serializers
from event.models import Artist, Event
from api.serializers.event_serializer import EventSerializer


class ArtistListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'age','description']


class ArtistListUseInEventFetch(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name']


class ArtistAddSerializer(serializers.ModelSerializer):
    """
    Artist Add serializer
    """
    name = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    description = serializers.CharField(required=True)
    
    class Meta:
        model = Artist
        fields = '__all__'
    
class ArtistEventSerializer(serializers.Serializer):
    """
    Event by Artist 
    """
    events = EventSerializer(many=True)
    artist = ArtistListUseInEventFetch()
    class Meta:
        fields = ['artist', 'events']
        
        

    


# class ArtistUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Artist
#         fields = '__all__'