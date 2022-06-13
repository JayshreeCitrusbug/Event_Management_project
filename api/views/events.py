from email import message
from multiprocessing import context
from django.http import HttpResponse
from api import serializers
from mysite import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, DestroyAPIView
from event.models import Event
from api.serializers import EventListingSerializer, EventAddSerializer, EventSerializer
# from mysite.permissions import get_pagination_response
from mysite.helpers import custom_response, get_object
from rest_framework import status
from mysite.permissions import MyPagination
from mysite.permissions import IsAccountOwner, IsAdminUser

class EventAPIView(APIView):
    def get(self,request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

class EventListingAPIView(ListAPIView):
    """
    Event listing View
    """
    queryset = Event.objects.filter(active=True)
    serializer_class = EventListingSerializer
    pagination_class = MyPagination


#Method -2 -> Use APIView
    # serializer_class = EventListingSerializer
    # def get(self, request):
    #     Events = Event.objects.filter(active=True)
    #     result = get_pagination_response(Events, request, self.serializer_class, context = {"request": request})
    #     message = "All Events data fetched Successfully!"
    #     return custom_response(True, status.HTTP_200_OK, message, result)


class EventDetailAPIView(APIView):
    """
    Retrieve, Event instance.
    """
    serializer_class = EventListingSerializer
    permission_classes = (IsAccountOwner,)

    # def get_object(self, pk):
    #     try:
    #         return Event.objects.get(pk=pk)
    #     except Event.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = EventListingSerializer(snippet)
    #     return response(serializer.data)

    def get(self, request, pk , format=None):

        # details = Event.objects.filter(id=pk)
        # serializer = self.serializer_class(details, data=request.data)
        # message = "Event Specific Detail fetched Successfully!"
        # result = serializer.data
        # return custom_response(True, status.HTTP_200_OK, message, result)

        event_detail = get_object(Event, pk)
        if not event_detail:
            message = "Event Does not exits..!!"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        serializer = self.serializer_class(event_detail, context={"request":request})
        message = "Event detali fetched Successfully!"
        return custom_response(True, status.HTTP_200_OK, message, serializer.data)
       
     
        
                
class EventAddAPIView(APIView):
    """
    Add, Event instance.
    """
    serializer_class = EventAddSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        # print("serializer data", serializer.initial_data)
        # print("is valid", serializer.is_valid())
        if serializer.is_valid():
            instance = serializer.save()
            instance.active = True
            instance.save()
            message = "Event generated successfully!"
            result = serializer.data
            # print("s",serializer.data)
            return custom_response(True, status.HTTP_200_OK, message, result)
        else:
            message = "Event can not generated please Try Again.."
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)

class EventUpdateAPIView(APIView):
    """
    Update, Event instance.
    """
    serializer_class = EventAddSerializer
    permission_classes = (IsAdminUser,)

    def patch(self, request, pk, format=None):
        events = get_object(Event, pk)
        if not events :
            message = "Event Does not exits..!!"
            return custom_response(True, status.HTTP_200_OK, message)
        serializer = self.serializer_class(events, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            message = "Event Updated Successfully!"
            result = serializer.data
            return custom_response(True, status.HTTP_200_OK, message, result)
        else:
            message = "Event can not Updated please Try Again.."
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        

class EventDeleteAPIView(DestroyAPIView):

    serializer_class = EventListingSerializer
    permission_classes = (IsAdminUser,)

    def delete(self, request, pk, format=None):
        snippet = Event.objects.get(pk=pk)
        serializer = self.serializer_class(snippet, data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            instance = serializer.save()
            instance.active = False
            instance.save()
            message = "Event Deleted successfully!"
            result = serializer.data
            return custom_response(True, status.HTTP_200_OK, message, result)
        else:
            message = "Event can not deleted please Try Again.."
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        
