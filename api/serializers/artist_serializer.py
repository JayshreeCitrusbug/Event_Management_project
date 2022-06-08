from rest_framework import fields, serializers
from event.models import Artist, Event


class ArtistListingSerializer(serializers.ModelSerializer):
    # name = serializers.SlugRelatedField(many= True, read_only = True, slug_field="name")
    class Meta:
        model = Artist
        fields = ['name', 'age']


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
    
class ArtistEventSerializer(serializers.ModelSerializer):
    """
    Artist data with Event
    """
    # event = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Artist
        fields = ['id']

    # def get_event(self,request):
    #     query = Event.objects.all()
    #     serializers = ArtistEventSerializer(query, many=False)
    #     return serializers.data


# class ArtistUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Artist
#         fields = '__all__'