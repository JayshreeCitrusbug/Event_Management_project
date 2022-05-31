from rest_framework import fields, serializers
from event.models import Event

class EventListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name','genre']