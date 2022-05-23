from django.db import models

# Create your models here.
from django.contrib.auth.models import User, PermissionsMixin
#from django.urls import reverse
from django.utils import timezone 

class Member(User,PermissionsMixin):
    event_admin = models.BooleanField(default=False)

    # class Meta:
    #     verbose_name = "User"
    #     verbose_name_plural = "Users"
        # ordering = ["-created_at"]
    # def __str__(self):
    #     return self.user.name 


class Artist(models.Model):
    name = models.CharField(max_length=50, blank=False)
    age = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = 'Artists'

    # def get_absolute_url(self):
    #     return reverse('event-list')
        # have to add template name here in reverse''


class Event(models.Model):
    name = models.CharField(max_length=150 , blank=False)
    genre =  models.ForeignKey('Genre', on_delete=models.CASCADE)
    eventDate =  models.DateTimeField()
    lastDateBook = models.DateTimeField()
    seatAvailable = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    description = models.TextField()
    artist = models.ManyToManyField(Artist)
    active = models.BooleanField()

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = 'Events'
    
    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('event-list')
        # have to add template name here in reverse''


class Genre(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class EventBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats = models.PositiveIntegerField()
    BookedDate = models.DateTimeField(default=timezone.now)
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)