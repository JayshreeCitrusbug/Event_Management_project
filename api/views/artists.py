from logging import exception
from rest_framework.response import Response
from rest_framework.views import APIView
from event.models import Artist
from api.serializers import ArtistListingSerializer,  ArtistAddSerializer
from mysite.permissions import get_pagination_response
from mysite.helpers import custom_response
from rest_framework import status


class ArtistListingAPIView(APIView):
    """
    Artist listing View
    """
    serializer_class = ArtistListingSerializer

    def get(self, request):
        testimonials = Artist.objects.all()
        result = get_pagination_response(testimonials, request, self.serializer_class, context = {"request": request})
        message = "ALL Artists data fetched Successfully!"
        return custom_response(True, status.HTTP_200_OK, message, result)

class ArtistDetailAPIView(APIView):
    """
    Retrieve, Artist instance.
    """
    serializer_class = ArtistListingSerializer

    def get(self, request, pk, format=None):
        details = Artist.objects.filter(pk=pk)
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

    def patch(self, request, pk, format=None):
        snippet = Artist.objects.get(pk=pk)
        serializer = self.serializer_class(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)