from rest_framework import fields, serializers
from rest_framework.response import Response
from event.models import Genre
# from api.serializers.event_serializer import EventSerializer

class GenreListingSerializer(serializers.ModelSerializer):
    # event_name = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ['id','name']
        
    # def get_event_name(self, pk):
    #     genre_event_query = Event.objects.filter(
    #             event_id=pk)
    #     serializer = EventSerializer(genre_event_query, many=True)
    
    #     return Response(serializer.data)