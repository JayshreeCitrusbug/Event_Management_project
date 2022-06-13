from .events import EventAPIView, EventListingAPIView, EventDetailAPIView, EventAddAPIView, EventUpdateAPIView, EventDeleteAPIView
from .artists import ArtistListingAPIView, ArtistDetailAPIView,  ArtistAddAPIView, ArtistUpdateAPIView, ArtistEventListAPIView
from .users import  SignUpApiView, LoginAPIView, LogoutAPIView, UserProfileAPI, UserListingAPIView
# UserListingAPIView,
from .genre import GenreListingAPIView, GenreAddAPIView, GenreUpdateAPIView, GenreEventAPIView
from .eventbook import EventBookListingAPIView, EventBookAddAPIView