from rest_framework import fields, serializers
from event.models import Artist

class ArtistListingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artist
        fields = '__all__'


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
    

# class ArtistUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Artist
#         fields = '__all__'