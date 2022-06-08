from cProfile import label
from dataclasses import fields
import email
from email.policy import default
from django.contrib.auth.forms import UserCreationForm
from django import forms
from event.models import EventBook, Member, User, Event, Artist
from django.contrib.auth.forms import ReadOnlyPasswordHashField


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


#............................................................................................................
class AccountUpdateForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("password",)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]



class AccountCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("email",)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(AccountCreationForm, self).save(commit=False)
        user.username = self.cleaned_data["email"]
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
#..............................................................................................................       
class UserUpdateForm(forms.ModelForm):
    """Custom form to change User"""

    class Meta():
        model = User

        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "username",
        ]

    def clean(self):
        cleaned_data = super(UserUpdateForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        last_name = cleaned_data.get("last_name")
        first_name = cleaned_data.get("first_name")

        if not email :
            raise forms.ValidationError(
                "Please add email."
            )
        if not password :
            raise forms.ValidationError(
                "Please add Password."
            )
        if not last_name :
            raise forms.ValidationError(
                "Please add last name."
            )
        if not first_name :
            raise forms.ValidationError(
                "Please add first name."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance
# .........................................................................................................
# User Creation form
class UserCreationForm(forms.ModelForm):
    """Custom User"""

    class Meta():
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "username",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        last_name = cleaned_data.get("last_name")
        first_name = cleaned_data.get("first_name")

        if not email :
            raise forms.ValidationError(
                "Please add email."
            )
        if not password :
            raise forms.ValidationError(
                "Please add Password."
            )
        if not last_name :
            raise forms.ValidationError(
                "Please add last name."
            )
        if not first_name :
            raise forms.ValidationError(
                "Please add first name."
            )
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance
        
#Add Event
class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude =['active']
        # fields = ['name', 'genre', 'eventDate', 'lastDateBook', 
        # 'seatAvailable', 'price', 'description', 'artist', 'active']
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
     
# class UpdateEventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         exclude =['active','eventDate','lastDateBook','price','seatAvailable']
#         # fields = ['name', 'genre', 'eventDate', 'lastDateBook', 
#         # 'seatAvailable', 'price', 'description', 'artist', 'active']

#         widgets = {
#             'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
#             'genre':forms.Select(attrs={'class':'form-select','placeholder':'Type of Event'}),
#             'eventDate':forms.DateTimeInput(attrs={'class':'form-control','placeholder':'Event Date in YYYY:MM:DD HH:MM:SS'}),
#             'lastDateBook':forms.DateTimeInput(attrs={'class':'form-control','placeholder':'Last Date of Booking in YYYY:MM:DD HH:MM:SS'}),
#             'seatAvailable':forms.NumberInput(attrs={'class':'form-control','placeholder':'No. of Seats Available'}),
#             'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Price per persion'}),
#             'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
#             'artist':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Select Artist'}),    
#             'active':forms.NullBooleanSelect(attrs={'class':'form-control','placeholder':'Active','default':'yes'}),
#         }

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

class EventBookForm(forms.ModelForm):
   
    class Meta:
        model = EventBook
        fields = ['seats','BookedDate','event_id']

        widgets = {
            'seats':forms.NumberInput(attrs={'class':'form-control','placeholder':'Select Seats'}),
            'event_id':forms.Select(attrs={'class':'form-select','placeholder':'Select Event'}),
    
        }
         # book = forms.ModelMultipleChoiceField(widget=forms.RadioSelect,queryset=EventBook.objects.all(),required=True)
        # class Meta:
        #     model = EventBook
        #     fields = ['seats','BookedDate','event_id']