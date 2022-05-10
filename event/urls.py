from django.urls import path, include
from . import views   
from event.views import EventListview, EventDetailView, UserRegisterView, Userprofile
# UserSignUpView

urlpatterns = [
    path('' , views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('price/',views.Price.as_view(), name='price'),
    path('contact',views.Contact.as_view(), name='contact'),
    #Register
    path('account/', include('django.contrib.auth.urls')),
    path('account/register/' , UserRegisterView.as_view(), name ='register'),
    # path('account/signup/', UserSignUpView.as_view(), name='signup'),  
    #Login
    path('account/eventlogin/', views.Login.as_view(), name='admin-login'),
    path('account/userprofile', Userprofile.as_view(), name='user-profile'),
    path('eventlist/' , EventListview.as_view(), name='event-list'),
    path('eventdetail/<int:pk>', EventDetailView.as_view(), name='event-detail'),
    
]