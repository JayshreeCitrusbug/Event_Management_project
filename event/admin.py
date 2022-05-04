from django.contrib import admin

# Register your models here.
from .models import Member, Artist, Event, Genre, EventBook


admin.site.register(Member)
admin.site.register(Artist)
admin.site.register(Event)
admin.site.register(Genre)
admin.site.register(EventBook)