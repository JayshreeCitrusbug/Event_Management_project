from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from event.models import Event
from api.serializers import EventListingSerializer
from mysite.permissions import get_pagination_response
from mysite.helpers import custom_response
from rest_framework import status


class EventListingAPIView(APIView):
    """
    Event listing View
    """
    serializer_class = EventListingSerializer

    def get(self, request):
        Events = Event.objects.filter(active=True)
        result = get_pagination_response(Events, request, self.serializer_class, context = {"request": request})
        message = "Events fetched Successfully!"
        return custom_response(True, status.HTTP_200_OK, message, result)


class EventDetail(APIView):
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
        details = Event.objects.filter(pk=pk)
        # details = self.get_object(pk)
        result = get_pagination_response(details, request, self.serializer_class, context = {"request": request})
        message = "Event Detail fetched Successfully!"
        return custom_response(True, status.HTTP_200_OK, message, result)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EventListingSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



    
