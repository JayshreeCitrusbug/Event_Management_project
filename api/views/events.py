from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from event.models import Event
from api.serializers import EventListingSerializer, EventAddSerializer, EventSerializer
from mysite.permissions import get_pagination_response
from mysite.helpers import custom_response
from rest_framework import status

class EventAPIView(APIView):
    def get(self,request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

class EventListingAPIView(APIView):
    """
    Event listing View
    """
    serializer_class = EventListingSerializer

    def get(self, request):
        Events = Event.objects.filter(active=True)
        result = get_pagination_response(Events, request, self.serializer_class, context = {"request": request})
        message = "All Events data fetched Successfully!"
        return custom_response(True, status.HTTP_200_OK, message, result)


class EventDetailAPIView(APIView):
    """
    Retrieve, Event instance.
    """
    serializer_class = EventListingSerializer


    # def get_object(self, pk):
    #     try:
    #         return Event.objects.get(pk=pk)
    #     except Event.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = EventListingSerializer(snippet)
    #     return response(serializer.data)

    def get(self, request, pk, format=None):
        # try:
        details = Event.objects.filter(id=pk)
            # details = self.get_object(pk)
        result = get_pagination_response(details, request, self.serializer_class, context = {"request": request})
        message = "Event Specific Detail fetched Successfully!"
        return custom_response(True, status.HTTP_200_OK, message, result)
        # except:
        #     if Event.objects.filter(pk=pk) not in Event.objects.filter('id'):
        #         message = "Event id not valid!"
        #         return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
                
class EventAddAPIView(APIView):
    """
    Add, Event instance.
    """
    serializer_class = EventAddSerializer

    def post(self, request):
        # serializer =self.serializer_class(request.POST)
        serializer = self.serializer_class(data=request.data)
        print("serializer data", serializer.initial_data)
        print("is valid", serializer.is_valid())
        if serializer.is_valid():
            instance = serializer.save()
            # print(serializer)
            instance.active = True
            instance.save()
            message = "Event generated successfully!"
            result = serializer.data
            print("s",serializer.data)
            return custom_response(True, status.HTTP_200_OK, message, result)
        else:
            message = "Event can not generated please Try Again.."
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)

class EventUpdateAPIView(APIView):
    """
    Update, Event instance.
    """
    serializer_class = EventAddSerializer

    def patch(self, request, pk, format=None):
        snippet = Event.objects.get(pk=pk)
        serializer = self.serializer_class(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



    
