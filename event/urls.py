from django.urls import path, include
from . import views   
from event.views import UserRegisterView, UserSignUpView, Userprofile, AdminProfileView, EventListview, EventDetailView, AddEventView, DeleteEventView, ArtistListview,ArtistDetailView, AddArtistView
app_name='customadmin'
urlpatterns = [
    path('' , views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('price/',views.Price.as_view(), name='price'),
    path('contact/',views.Contact.as_view(), name='contact'),
    #Register
    path('account/', include('django.contrib.auth.urls')),
    path('account/register/' , UserRegisterView.as_view(), name ='register'), #Admin
    path('account/signup/', UserSignUpView.as_view(), name='signup'),  #User
    #Login
    path('account/eventlogin/', views.Login.as_view(), name='login'),
    #Dashboard
    path('dashboard/',views.AdminProfileView.as_view(), name='dashboard'),
    #Admin pannel event artist page
    path('events/', views.Eventview.as_view(), name = 'admin-event-view'),
    path('artist/', views.Artistview.as_view(), name = 'admin-artist-view'),
    #Profile
    path('account/userprofile/', Userprofile.as_view(), name='user-profile'),
    path('account/adminprofile/', AdminProfileView.as_view(), name='admin-profile'),
    #User 
    path("users/", views.UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/detail/", views.UserDetailView.as_view(), name="user-detailview"),
    #Logout
    path('account/logout/', views.Logout.as_view(),{'next_page': 'home'}, name='logout'),
    ##Event
    path('event/list/' , EventListview.as_view(), name='event-list'),
    path('event/detail/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
        #Add Event
    path('event/add/', AddEventView.as_view(), name='add-event'),
        #Update event
    path('event/update/<int:pk>/', views.UpdateEventView.as_view(), name='update-event'),
        #Delete event
    path('event/delete/<int:pk>/', DeleteEventView.as_view(), name='delete-event'),
    path('event/booked/', views.EventBookView.as_view(), name='event-booked'),
    ##Artist
    path('artist/list/' , ArtistListview.as_view(), name='artist-list'),
    path('artist/detail/<int:pk>/', ArtistDetailView.as_view(), name='artist-detail'),
        #Add Artist
    path('artist/add/', AddArtistView.as_view(), name='add-artist'),
    path('artist/update/<int:pk>/', views.UpdateArtistView.as_view(), name='update-artist'),
]