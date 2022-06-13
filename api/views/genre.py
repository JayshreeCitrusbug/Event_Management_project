from django.http import JsonResponse
from api import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from event.models import Genre, Event
from api.serializers import GenreListingSerializer, GenreAddSerializer, GenreEventSerializer
from mysite.permissions import get_pagination_response
from mysite.helpers import custom_response, get_object
from django.shortcuts import get_object_or_404
from rest_framework import status
from mysite.permissions import MyPagination
from mysite.permissions import IsAccountOwner, IsAdminUser

class GenreListingAPIView(ListAPIView):
    """
    Genre listing View
    """
    
    queryset = Genre.objects.all()
    serializer_class = GenreListingSerializer
    pagination_class = MyPagination

    # def get(self, request):
    #     geners = Genre.objects.all()
    #     serializer = GenreListingSerializer(geners, many =True)
    #     return Response(serializer.data)
        

class GenreAddAPIView(APIView):
    """
    Genre Create View
    """
    serializer_class = GenreAddSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            message = "Genre Created successfully!"
            result = serializer.data
            return custom_response(True, status.HTTP_200_OK, message, result)
        else:
            message = "Genre can not generated please Try Again.."
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)


class GenreUpdateAPIView(APIView):
    """
    Update, Artist instance.
    """
    serializer_class = GenreAddSerializer
    permission_classes = (IsAdminUser,)

    def patch(self, request, pk):
        genres = get_object(Genre, pk)
        if not genres :
            message = "Gener Does not exits..!!"
            return custom_response(True, status.HTTP_200_OK, message)
        serializer = self.serializer_class(genres, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            message = "Genre Updated Successfully!"
            result = serializer.data
            return custom_response(True, status.HTTP_200_OK, message, result)
        else:
            message = "Genre can not Updated please Try Again.."
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreEventAPIView(APIView):
    """
    Fetch event by Genre
    """
    serializer_class = GenreEventSerializer
    # def queryset(self):
       
    #     return genre_data
    
    def get(self, request):
        genre_data = Genre.objects.all()
        print('genre_data', genre_data)
        event_data =[]
        main_dict = {}
        for g in genre_data:
            eve_obj = Event.objects.filter(genre = g)
            main_dict = {"genre": g ,"events": eve_obj}
            print(main_dict)
            print(type(main_dict))
            serializer = GenreEventSerializer(main_dict)
            event_data.append(serializer.data)
        return Response(event_data)
    


        # 
        # print('event_data',event_data)

  
        # geners = Genre.objects.all()
        # serializer = GenreListingSerializer(geners, many =True)
        # return Response(serializer.data)
    # main_dict = {"genre": obj, "events": <qs>}
# >.................................................................................. CHANGE logic........................................................................<
    # def get (self, request):
    #     main_dict = {}
    #     event_data = Event.objects.all()
    #     genre_data = Genre.objects.all()
    #     # print('genre_data', genre_data)
    #     for genre in genre_data:
    #         if str(genre.id) in main_dict.keys():
    #             main_dict(str(genre.id)).append(genre.name)
    #         else:
    #             main_dict[str(genre.id)] = [genre.name]
                
    #             for event in event_data:
                
    #                 if genre == event.genre:
    #                     if str(genre.name) in main_dict.keys():
    #                         main_dict[genre.name].append(event)
                
    #                     else:
    #                         main_dict[genre.name] = [event]

    #     print('genre_dict',main_dict)
    
    #     serializer = GenreEventSerializer(main_dict)
    #     return Response(serializer.data)
    
#>...........................................................................................<
    # def get(self, request):
    #     genre = Genre.objects.all()
    #     serializer = self.serializer_class(genre)

    #     return Response(serializer.data)

