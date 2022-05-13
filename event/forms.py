from cProfile import label
from dataclasses import fields
import email
from email.policy import default
from django.contrib.auth.forms import UserCreationForm
from django import forms
from event.models import Member, User, Event, Artist


#Admin Register form
class UserNewCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Member
        fields = ["username", "first_name", "last_name", "email","password1","password2"]

    def clean(self):
        print(super(UserNewCreationForm, self).clean())
        return  super(UserNewCreationForm, self).clean()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.event_admin = True
        if commit:
            user.is_staff = True
            user.save()
        return user
#END Admin Register form


#User Register Form
class UserSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1","password2"]

    def save(self):
        user = super().save(commit=False)
        user.event_admin = False
        user.save()
        return user   
#END User Register Form


#Login for both
class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
#END Login


        


#Add Event
class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        # exclude =['active']
        fields = ['name', 'genre', 'eventDate', 'lastDateBook', 
        'seatAvailable', 'price', 'description', 'artist', 'active']
        label = {
            'name':'',
            'genre':'',
            'eventDate':'',
            'lastDateBook':'',
            'seatAvailable':'',
            'price':'',
            'description':'',
            'artist':'',
            'active':'',
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'genre':forms.Select(attrs={'class':'form-select','placeholder':'Type of Event'}),
            'eventDate':forms.DateTimeInput(attrs={'class':'form-control','placeholder':'Event Date in YYYY:MM:DD HH:MM:SS'}),
            'lastDateBook':forms.DateTimeInput(attrs={'class':'form-control','placeholder':'Last Date of Booking in YYYY:MM:DD HH:MM:SS'}),
            'seatAvailable':forms.NumberInput(attrs={'class':'form-control','placeholder':'No. of Seats Available'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Price per persion'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'artist':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Select Artist'}),    
            'active':forms.NullBooleanSelect(attrs={'class':'form-control','placeholder':'Active','default':'yes'}),
        }
     
class UpdateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude =['active','eventDate','lastDateBook','price','seatAvailable']
        # fields = ['name', 'genre', 'eventDate', 'lastDateBook', 
        # 'seatAvailable', 'price', 'description', 'artist', 'active']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'genre':forms.Select(attrs={'class':'form-select','placeholder':'Type of Event'}),
            'eventDate':forms.DateTimeInput(attrs={'class':'form-control','placeholder':'Event Date in YYYY:MM:DD HH:MM:SS'}),
            'lastDateBook':forms.DateTimeInput(attrs={'class':'form-control','placeholder':'Last Date of Booking in YYYY:MM:DD HH:MM:SS'}),
            'seatAvailable':forms.NumberInput(attrs={'class':'form-control','placeholder':'No. of Seats Available'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Price per persion'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'artist':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Select Artist'}),    
            'active':forms.NullBooleanSelect(attrs={'class':'form-control','placeholder':'Active','default':'yes'}),
        }

#Artist 

class AddArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
       
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Artist Name'}),
            'age':forms.NumberInput(attrs={'class':'form-control','placeholder':'Artist Age'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            
        }