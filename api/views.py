from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from event.models import *
from api.serializers import *

# Create your views here.
class EventGet(APIView):
    def get(self,request):
        Events = Event.objects.all()
        serializer = EventListingSerializer(Events , many=True)
        return Response(serializer.data)


class ArtistGet(APIView):
    def get(self,request):
        Artists = Artist.objects.all()
        serializer = ArtistListingSerializer(Artists , many=True)
        return Response(serializer.data)


class UserGet(APIView):
    def get(self,request):
        Users = User.objects.all()
        serializer = UserListingSerializer(Users , many=True)
        return Response(serializer.data)
