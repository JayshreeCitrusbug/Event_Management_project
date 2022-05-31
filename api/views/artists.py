from rest_framework.views import APIView
from event.models import Artist
from api.serializers import ArtistListingSerializer
from mysite.permissions import get_pagination_response
from mysite.helpers import custom_response
from rest_framework import status


class ArtistListingAPIView(APIView):
    """
    Event listing View
    """
    serializer_class = ArtistListingSerializer

    def get(self, request):
        testimonials = Artist.objects.all()
        result = get_pagination_response(testimonials, request, self.serializer_class, context = {"request": request})
        message = "Artists fetched Successfully!"
        return custom_response(True, status.HTTP_200_OK, message, result)