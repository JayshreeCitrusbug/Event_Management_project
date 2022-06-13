from rest_framework import fields, serializers
from event.models import EventBook
from rest_framework.authtoken.models import Token


class EventBookListSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = EventBook
        fields = '__all__'
        # depth = 2

    # def get_token(self, obj):
    #     return f"Token {Token.objects.get_or_create(user=obj)[0]}"

class EventBookSerializer(serializers.ModelSerializer):
    """
    Book Event Serializer
    """
    class Meta:
        model = EventBook
        fields = '__all__'

    def get_token(self, obj):
        return f"Token {Token.objects.get_or_create(user=obj)[0]}"