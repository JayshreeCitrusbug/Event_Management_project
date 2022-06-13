import datetime
from logging import exception
from multiprocessing import context
from reprlib import aRepr
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from event.models import Artist, Event
from api.serializers import ArtistListingSerializer, ArtistAddSerializer, ArtistEventSerializer
# from mysite.permissions import get_pagination_response
# from mysite.permissions import PageNumberPagination

from mysite.helpers import custom_response, get_object
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from mysite.permissions import MyPagination
from mysite.permissions import IsAccountOwner, IsAdminUser
import json


class ArtistListingAPIView(ListAPIView):
    """
    Artist listing View
    """
#Method -1 -> Use ListAPIView
    queryset = Artist.objects.all()
    serializer_class = ArtistListingSerializer
    pagination_class = MyPagination

#Method -2 -> Use APIView
    
    # serializer_class = ArtistListingSerializer
    # def get(self, request):
    #     lists = Artist.objects.all()
    #     page_size = request.data['limit']
        
    #     result = get_pagination_response(lists, request,self.serializer_class,  page_size, context = {"request": request})

    #     message = "Artist list fetched Successfully!"
    #     return custom_response(True, status.HTTP_200_OK, message, result)
    
#Method -3 -> Use APIView
    # def get(self, request):
    #     artists = Artist.objects.all()
    #     queryset = ArtistListingSerializer(artists, many=True)
    #     return Response(queryset.data)


class ArtistDetailAPIView(APIView):
    """
    Retrieve, Artist instance.
    """
    serializer_class = ArtistListingSerializer
    permission_classes = (IsAccountOwner,)

    def get(self, request, pk, format=None):
        artist_detail = get_object(Artist, pk)
        if not artist_detail:
            message = "Artist Does not exits..!!"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        serializer = self.serializer_class(artist_detail, context={"request":request})
        message = "Artist detail fetched Successfully!"
        return custom_response(True, status.HTTP_200_OK, message, serializer.data)
       
    

class ArtistAddAPIView(APIView):
    """
    Add, Event instance.
    """
    serializer_class = ArtistAddSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
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
    permission_classes = (IsAdminUser,)


    #Method writtten in helpers.py
    # def get_object(self, pk):
    #     try:
    #         return Artist.objects.get(pk=pk)
    #     except exception as e:
    #         return f'Error, {e}'

    def patch(self, request, pk, format=None):
        artists = get_object(Artist, pk)
        if not artists :
            message = "Artist Does not exits..!!"
            return custom_response(True, status.HTTP_200_OK, message)
        serializer = self.serializer_class(artists, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            message = "Artist Updated Successfully!"
            result = (serializer.data)
            return custom_response(True, status.HTTP_200_OK, message, result)
        else:
            message = "Artist can not Updated please Try Again.."
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


        
        
       
    