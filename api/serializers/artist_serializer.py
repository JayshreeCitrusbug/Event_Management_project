from rest_framework import fields, serializers
from event.models import Artist

class ArtistListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'