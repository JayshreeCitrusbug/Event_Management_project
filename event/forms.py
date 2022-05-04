from email.policy import default
from django.contrib.auth.forms import UserCreationForm
from django import forms

from event.models import Member, User

class UserNewCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Member

    def save(self, commit=True):
        user = super().save(commit=False)
        user.event_admin = True
        if commit:
            user.save()
        return user



class UserSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.event_admin = False
        user.save()
       
        return user   