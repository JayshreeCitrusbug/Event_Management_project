from imaplib import _Authenticator
from re import template
from types import MemberDescriptorType
from urllib import request
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

# Create your views here.
from django.views.generic import View, ListView, DetailView, CreateView
from event import forms
from event.models import Event, Artist, EventBook, Genre, Member , User
from django.contrib.auth.models import auth
from event.forms import  UserNewCreationForm,  AdminLoginForm
# UserSignUpForm,
from django.contrib import messages

#from django.views import generic
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy



#Home page
class Home(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
#About Page
class About(View):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
#Price
class Price(View):
    template_name = "event/price.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

#User Profile
class Userprofile(ListView):
    model = Event
    template_name = "account/userprofile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


#Contact Page
class Contact(View):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})



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
    
    def post(self, request):
        print("request",request.POST)
        form = self.form_class(request.POST)
        errors = form.non_field_errors()
        field_errors = [ (field.label, field.errors) for field in form]
        print("field_errors", field_errors) 
        
        print('Form is', form.is_valid())
        if form.is_valid():
            form.save()
            # msg = "form is valid data is added in db"
            # return HttpResponse(msg)
            return redirect('admin-login')
        else:
            msg = "ERROR -->>> form is not valid"
            return HttpResponse(msg)
        
#END Admin Register

#User Register
# class UserSignUpView(CreateView):
#     model = User
#     form_class = UserSignUpForm
#     template_name = 'account/usersignup.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'user'
#         return super().get_context_data(**kwargs)

#     def post(self, request):
#         form = self.form_class(request.POST)
#         # print(form.cleaned_data)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             return redirect('event-list')

#END User Register
#END Register view

#Login View
#Admin Login View
class Login(View):
    model = Member
    template_name = "account/adminlogin.html"   
    form_class = AdminLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            un = form.cleaned_data.get('username')
            psw = form.cleaned_data.get('password')
            user =  auth.authenticate(username=un,password=psw)
            try:
                if user is not None:
                    if user.is_active and user.is_staff == True:
                        return render(request, 'account/adminprofile.html') 
                    else:
                        auth.login(request,user)
                        return render(request,'account/userprofile.html')
                else:
                    msg = 'If New User than please register first..!!'
                    return render(request, self.template_name, context={'form':form , 'message':msg})

            except Exception as e:
                message = f'Error, either Email or Password is not correct  {e}'
                return HttpResponse(message)

                
        else:
            form = self.form_class()
            return render(request, self.template_name, {'form':form})

