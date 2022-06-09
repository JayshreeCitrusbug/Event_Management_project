import datetime
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
from django.shortcuts import get_object_or_404, render
from rest_framework import status
import json


class ArtistListingAPIView(APIView):
    """
    Artist listing View
    """
    # serializer_class = ArtistListingSerializer

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
        artists = Artist.objects.get(pk=pk)
        serializer = self.serializer_class(artists, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtistEventListAPIView(APIView):
    """
    Fetch Event data from Artist name.
    """
    serializer_class = ArtistEventSerializer
    
    def get(self, request):
        artist_data = Artist.objects.all()
        print('artist_data', artist_data)
        event_data =[]
        main_dict = {}
        for a in artist_data:
            eve_obj = Event.objects.filter(artist = a)
            main_dict = {"artist": a ,"events": eve_obj}
            print(main_dict)
            print(type(main_dict))
            serializer = ArtistEventSerializer(main_dict)
            event_data.append(serializer.data)
        return Response(event_data)

    
    # def get(self,request):
       
    #     event_data = Event.objects.all()
    #     event_dict = {}
    #     artist_dict = {}
        
    #     for events in event_data:
    #         if events.id in event_dict.keys():
    #             event_dict[events.id].append(events)
    #         else:
    #             event_dict[events.id] = [events]
        
        
        
    # serializer_class = ArtistEventSerializer

    # def get(self, request):
        
    #     artist_data = Artist.objects.all()
    #     event_data = Event.objects.filter(active=True)
    #     event_dict = {}
    #     for events in event_data:
    #         if events.id in event_dict.keys():
    #             event_dict[events.id].append(events)
    #         else:
    #             event_dict[events.id] = [events]
    #     result = get_pagination_response(event_dict, request, self.serializer_class, context = {"request": request})
    #     message = "All Events data fetched Successfully!"
    #     return custom_response(True, status.HTTP_200_OK, message, result)
        
        
        # try:
        #     eventJSONData = json.dumps(event_dict, default=lambda value: value.__dict__, sort_keys=True, indent=4)

        # except:
        #         def json_default(value):
        #             eventJSONData = json.dumps(event_dict, default=lambda value: value.__dict__, sort_keys=True, indent=4)
        #             if isinstance(eventJSONData, datetime.datetime):
        #                 return dict(year=eventJSONData.year, month=eventJSONData.month, day=eventJSONData.day)
        #             else:
        #                 return value.__dict__
        # for artists in artist_data:
        #     if artists.id in artist_dict.keys():
        #         artist_dict[artists.id].append(artists)
        #     else:
        #         artist_dict[artists.id] = [artists]
        # artistJSONData = json.dumps(artist_dict, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        # serializer = ArtistEventSerializer(artist_data, many=True)
        # eventJSONData={}
        # artistJSONData={}
        # print("event_dict",event_dict)
        # print("artist_dict",artist_dict)
        # for i in event_dict:
            # return(eventJSONData(json.dumps(i)))
        # print(eventJSONData)
        # serializer = self.serializer_class(event_dict, many=True)
        # context = {"eventJSONData":eventJSONData, "serializer":serializer.data}
        # print("context",context)


        
        
       
    