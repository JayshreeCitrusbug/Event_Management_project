from re import template
from types import MemberDescriptorType
from urllib import request
from django import forms
from django.shortcuts import redirect, render

# Create your views here.
from django.views.generic import View, ListView, DetailView, CreateView
from event import forms
from event.models import Event, Artist, EventBook, Genre, Member , User
from event.forms import UserSignUpForm, UserNewCreationForm, AdminLogin
from django.contrib import messages

#from django.views import generic
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy



#Main page
class main(View):
    template_name = "event/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
#method base view of  main      
# def main(request):
#     return render(request, 'event/home.html' , {})


#Profile
#..............................................??????????????????Have to check return statement............return none value error occured????????
class AdminLogin(View):
    model = User
    template_name = "account/adminlogin.html"   
    form_class = AdminLogin
    def get(self, request):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = User.objects.create_user(email, password)
                try:
                    user = User.objects.get(email=email, password=password)
                    return render(request, 'event/home.html', {'user':user})
                except:
                    messages.success(request, 'Error, either Email or Password is not correct')
            else:
                form = AdminLogin()
            return render(request, self.template_name)

#..............................................??????????????????????????????????
    

#Event list/Detail view
class EventListview(ListView):
    model = Event
    template_name = 'event/event_list.html'

class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event_detail.html'

# END Event list Detail view

#Register view
#Admin Register
class UserRegisterView(CreateView):
    model = Member
    form_class = UserNewCreationForm
    template_name = 'account/register.html'

    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'event_admin'
    #     return super().get_context_data(**kwargs)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-login')
        else:
            return redirect('event-list')


#User Register
class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'account/usersignup.html'

    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'user'
    #     return super().get_context_data(**kwargs)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('event-list')
#END Register view