from api import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from event.models import Genre
from api.serializers import GenreListingSerializer

from rest_framework import status

class GenreListingAPIView(APIView):
    """
    Event listing View
    """
    serializer_class = GenreListingSerializer

    def get(self, request):
        geners = Genre.objects.all()
        serializer = GenreListingSerializer(geners, many =True)
        return Response(serializer.data)
        # result = get_pagination_response(geners, request, self.serializer_class, context = {"request": request})
        # message = "All Genres data fetched Successfully!"
        # return custom_response(True, status.HTTP_200_OK, message, result)
