from rest_framework.views import APIView
from event.models import User
from api.serializers import UserListingSerializer, UserRegisterSerializer, UserLoginSerializer
from mysite.permissions import get_pagination_response
from mysite.helpers import custom_response, serialized_response, get_object
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from mysite.permissions import IsAccountOwner
import math
import datetime
import random


class UserListingAPIView(APIView):
    """
    User listing View
    """
    serializer_class = UserListingSerializer

    def get(self, request):
        testimonials = User.objects.filter(is_active=True)
        result = get_pagination_response(testimonials, request, self.serializer_class, context = {"request": request})
        message = "All Users data fetched Successfully!"
        return custom_response(True, status.HTTP_200_OK, message, result)



class SignUpApiView(APIView):
    """
    User Sign up view
    """
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        if 'email' in request.data:
            email_check = User.objects.filter(email=request.data['email']).distinct()
            if email_check.exists():
                message = "Email already exists!"
                return custom_response(True, status.HTTP_400_BAD_REQUEST, message)
            message = "Account created successfully!"
            serializer = self.serializer_class(data=request.data, context={'request': request})
            response_status, result, message = serialized_response(serializer, message)
            status_code = status.HTTP_201_CREATED if response_status else status.HTTP_400_BAD_REQUEST
            # TODO Email
            return custom_response(response_status, status_code, message, result)
        else:
            return custom_response(False, status.HTTP_400_BAD_REQUEST, "Email is required")


class LoginAPIView(APIView):
    """
    User Login View
    """
    serializer_class = UserLoginSerializer
    
    def post(self, request, format=None):
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        account = authenticate(username=username, password=password)
        
        if account is not None:
            login(request, account)
            serializer = self.serializer_class(account, context={'request':request})
            return custom_response(True, status.HTTP_200_OK, "Login Successful!", serializer.data)
        else:
            message = "UserName/password combination invalid"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)


class LogoutAPIView(APIView):
    """
    User Logout View
    """
    permission_classes = (IsAccountOwner,)

    def post(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        message = "Logout successful!"
        return custom_response(True, status.HTTP_200_OK, message)


class UserProfileAPI(APIView):
    """
    User Profile view
    """
    serializer_class = UserRegisterSerializer
    permission_classes = (IsAccountOwner,)

    def put(self, request, *args, **kwargs):
        user_profile = get_object(User, request.user.pk)
        if not user_profile:
            message = "User not found!"
            return custom_response(True, status.HTTP_200_OK, message)
        message = "User Profile updated successfully!"
        serializer = self.serializer_class(user_profile, data=request.data, partial=True, context={"request": request})
        response_status, result, message = serialized_response(serializer, message)
        status_code = status.HTTP_201_CREATED if response_status else status.HTTP_400_BAD_REQUEST
        return custom_response(response_status, status_code, message, result)

    def get(self, request):
        user_profile = get_object(User, request.user.pk)
        if not user_profile:
            message = "Requested account details not found!"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        serializer = self.serializer_class(user_profile, context={"request": request})
        message = "User Profile fetched Successfully!"
        return custom_response(True, status.HTTP_200_OK, message, serializer.data)