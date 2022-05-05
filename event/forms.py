from dataclasses import fields
import email
from email.policy import default
from django.contrib.auth.forms import UserCreationForm
from django import forms

from event.models import Member, User

#Admin Register form
class UserNewCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Member
        fields = ["username", "first_name", "last_name", "email"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.event_admin = True
        if commit:
            user.is_staff = True
            user.save()
        return user

class AdminLogin(forms.Form):
    email = forms.CharField(max_length=150)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
#END Admin Register form


#User Register Form
class UserSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def save(self):
        user = super().save(commit=False)
        user.event_admin = False
        user.save()
        return user   
#END User Register Form


class AdminLogin(forms.Form):
    email = forms.EmailField(max_length=150)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)