from api import serializers
from mysite import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from event.models import EventBook, Event
from api.serializers import EventBookListSerializer, EventBookSerializer
from mysite.helpers import custom_response, get_object
from rest_framework import status
from mysite.permissions import MyPagination
from mysite.permissions import IsAccountOwner, IsAdminUser


class EventBookListingAPIView(ListAPIView):
    queryset = EventBook.objects.all()
    serializer_class = EventBookListSerializer


class EventBookAddAPIView(APIView):
    """
    Book Event Api View
    """
    serializer_class = EventBookSerializer
    permission_classes = (IsAccountOwner,)

    def post(self, request, format=None):

        seats = request.data.get("seats", None)
        event_id = request.data.get("event_id", None)
        serializer = self.serializer_class(data=request.data)
        fetch_event = Event.objects.get(id = event_id)
        total_seat = fetch_event.seatAvailable
        print('BEFORE total_seat',total_seat)

        final_avl = int(total_seat) - int(seats)
        # fseat = Event.objects.filter(id = event_id).update(seatAvailable = final_avl)
        fetch_event.seatAvailable = final_avl
        fetch_event.save()
        print('seats',seats)
        print('event_id',event_id)
        print('AFTER fetch_event', fetch_event)
        print('seatAvailable',fetch_event)
        print('final_avl',final_avl)

        if serializer.is_valid():
            instance = serializer.save()
            instance.user_id = request.user.pk
            instance.save()
            message = "Event Booked successfully!"
            result = serializer.data
            return custom_response(True, status.HTTP_200_OK, message, result)
        else:
            message = "Event Cannot Booked please Try Again.."
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
            # instance.user = request.user.pk