from django.urls import path, include
from . import views   
from event.views import EventListview, EventDetailView, UserRegisterView
# UserSignUpView

urlpatterns = [
    path('' , views.main.as_view(), name='home'),
    #Register
    path('account/', include('django.contrib.auth.urls')),
    path('account/register/' , UserRegisterView.as_view(), name ='register'),
    # path('account/signup/', UserSignUpView.as_view(), name='signup'),  
    #Login
    path('account/eventadminlogin/', views.AdminLogin.as_view(), name='admin-login'),
    path('event/' , EventListview.as_view(), name='event-list'),
    path('eventdetail/<int:pk>', EventDetailView.as_view(), name='event-detail'),
    
]