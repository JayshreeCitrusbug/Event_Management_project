from rest_framework import fields, serializers
from event.models import Artist
from rest_framework.authtoken.models import Token
from api.serializers.event_serializer import EventSerializer


class ArtistListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'age','description']

    def get_token(self, obj):
        return f"Token {Token.objects.get_or_create(user=obj)[0]}"


class ArtistListUseInEventFetch(serializers.ModelSerializer):
    # for set field to name only
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
    
    def get_token(self, obj):
        return f"Token {Token.objects.get_or_create(user=obj)[0]}"

    
class ArtistEventSerializer(serializers.Serializer):
    """
    Event Details by Artist 
    """
    events = EventSerializer(many=True)
    artist = ArtistListUseInEventFetch()
    class Meta:
        fields = ['artist', 'events']
        
        

    


# class ArtistUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Artist
#         fields = '__all__'