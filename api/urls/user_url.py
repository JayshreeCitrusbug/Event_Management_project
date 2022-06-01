from django.urls import path
from .. import  views

urlpatterns = [
    path("users/", views.UserListingAPIView.as_view(), name='users'),
    path("register/", views.SignUpApiView.as_view(), name="signup"),
    path("login/", views.LoginAPIView.as_view(), name='login'),
    path("logout/", views.LogoutAPIView.as_view(), name="logout"),
    path("profile/", views.UserProfileAPI.as_view(), name="profile"),
]