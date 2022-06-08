from logging import exception
from multiprocessing import context
from reprlib import aRepr
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from event.models import Artist, Event
from api.serializers import ArtistListingSerializer, ArtistAddSerializer, ArtistEventSerializer
from mysite.permissions import get_pagination_response
from mysite.helpers import custom_response
from django.shortcuts import get_object_or_404
from rest_framework import status


class ArtistListingAPIView(APIView):
    """
    Artist listing View
    """
    serializer_class = ArtistListingSerializer

    def get(self, request):
        artists = Artist.objects.all()
        # event = Event.objects.all()

        queryset = ArtistListingSerializer(artists, many=True)
        return Response(queryset.data)
        # result = get_pagination_response(artists, request, self.serializer_class, context = {"request": request})
        # message = "ALL Artists data fetched Successfully!"
        # return custom_response(True, status.HTTP_200_OK, message, result)


    # def list(self, request):
    #     queryset = Artist.objects.all()
    #     serializer = ArtistListingSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Artist.objects.all()
    #     artist = get_object_or_404(queryset, pk=pk)
    #     serializer = ArtistListingSerializer(artist)
    #     return Response(serializer.data)

class ArtistDetailAPIView(APIView):
    """
    Retrieve, Artist instance.
    """
    serializer_class = ArtistListingSerializer

    def get(self, request, pk, format=None):
        details = Artist.objects.filter(id=pk)
        result = get_pagination_response(details, request, self.serializer_class, context = {"request": request})
        message = "Artist Specific Detail fetched Successfully!"
        return custom_response(True, status.HTTP_200_OK, message, result)



class ArtistAddAPIView(APIView):
    """
    Add, Event instance.
    """
    serializer_class = ArtistAddSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.POST)
        if serializer.is_valid():
            serializer.save()
            message = "Artist Created successfully!"
            result = serializer.data
            return custom_response(True, status.HTTP_200_OK, message, result)
        else:
            message = "Artist can not generated please Try Again.."
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)


class ArtistUpdateAPIView(APIView):
    """
    Update, Artist instance.
    """
    serializer_class = ArtistAddSerializer
    # def get_object(self, pk):
    #     try:
    #         return Artist.objects.get(pk=pk)
    #     except exception as e:
    #         return f'Error, {e}'

    def patch(self, request, pk):
        snippet = Artist.objects.get(pk=pk)
        serializer = self.serializer_class(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtistEventListAPIView(APIView):
    """
    Fetch Event data from Artist name.
    """
    # serializer_class = ArtistEventSerializer
    def get(self,request):
        artist_data = Artist.objects.all()
        event_data = Event.objects.all()
        event_dict = {}
        artist_dict = {}
        
        for events in event_data:
            if events.id in event_dict.keys():
                event_dict[events.id].append(events)
            else:
                event_dict[events.id] = [events]

        for artists in artist_data:
            if artists.id in artist_dict.keys():
                artist_dict[artists.id].append(artists)
            else:
                artist_dict[artists.id] = [artists]
        
            
        print("event_dict",event_dict)
        print("artist_dict",artist_dict)
        context = {'artist_dict':artist_dict, 'event_dict':event_dict}
        print("context",context)


        serializer = ArtistEventSerializer(context, many=True)
        return Response(serializer.data)
       
    