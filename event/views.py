from imaplib import _Authenticator
from re import template
from types import MemberDescriptorType
from urllib import request
from django import forms, views
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import View, ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from event import forms
from event.models import Event, Artist, EventBook, Genre, Member , User
from django.contrib.auth.models import auth
from event.forms import  UserNewCreationForm, UserSignUpForm,  AdminLoginForm, AddEventForm, UpdateEventForm, AddArtistForm
# ,  AdminProfileForm

from django.contrib import messages

#from django.views import generic
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy



#Home page
class Home(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        # un1=request.POST['username']
        # user1 = User.objects.get(username=un1)
        # print(user1)
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

#Contact Page
class Contact(View):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})






#User Profile
class Userprofile(ListView):
    model = Event
    template_name = "account/userprofile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


#Admin Profile View
class AdminProfileView(ListView):
    model = Event
    template_name = "account/adminprofile.html"
    un = Member.objects.select_related('user_ptr').all()
    print('member data' ,un)
    def get(self, request):
        eventData = Event.objects.all()
        # artistname = Artist.objects.all()  ,'showartist':artistname print('artist data', artistname)
        print('evenrdata',eventData)
        print(type(eventData))
        # lst = list(eventData.values())
        # print(type(lst))
        return render(request,self.template_name,{'showevent':eventData})


        


#Event list/Detail view
class EventListview(ListView):
    model = Event
    template_name = 'event/event_list.html'
   
class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event_detail.html'

class EventBooked(View):
    model = EventBook
    template_name = 'event/eventbook.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

class AddEventView(CreateView):
    model = Event
    form_class = AddEventForm
    template_name = 'event/add_event.html'

    def post(self, request):
        form =self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event-list')
        else:
            msg = "Event can not generated please Try Again "
            return HttpResponse(msg)

class UpdateEventView(UpdateView):
    model = Event
    form_class = UpdateEventForm
    template_name = 'event/update_event.html'
    

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form':self.form_class})

    def get_success_url(self):
         return reverse_lazy('admin-profile')


class DeleteEventView(DeleteView):
    model = Event
    template_name = 'event/delete_event.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'name':Event.name})

    def get_success_url(self):
         return reverse_lazy('admin-profile')
# ............................................................
# class UpdateEventView(UpdateView):
#     model = Event
#     form_class = UpdateEventForm
#     template_name = 'event/update_event.html'
    

#     def get(self, request, *args, **kwargs):
#         form = self.form_class
#         data = Event.objects.get(self.kwargs['pk'])
#         return render(request, self.template_name, {'form':form, 'data':data})
    
#     context_object_name = 'data'
    
#     def get_success_url(self):
#         return reverse_lazy('event-list')

# class UpdateEvent(View):
#     model = Event
#     form_class = UpdateEventForm
#     template_name = 'event/update_event.html'
    

#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, {'form':self.form_class})

#     def post(self, request, event_id):
#         event = Event.objects.get(pk=event_id)
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('event-list')
#         return render(request, 'update-event', {'form':form})
# ............................................................

# END Event list Detail view



#Artist list detail View

class ArtistListview(ListView):
    model = Artist
    template_name = 'artist/artist_list.html'

class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artist/artist_detail.html'

class AddArtistView(CreateView):
    model = Artist
    form_class = AddArtistForm
    template_name = 'artist/add_artist.html'

    def post(self, request):
        form =self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artist-list')
        else:
            msg = "Artist can not generated please Try Again later. "
            return HttpResponse(msg)



# class UpdateArtistView(UpdateView):
#     model = Event
#     form_class = UpdateArtistForm
#     template_name = 'event/update_event.html'
    

#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, {'form':self.form_class})

#     def get_success_url(self):
#          return reverse_lazy('admin-profile')













#END Artist list detail View



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
            return redirect('login')
        else:
            msg = "ERROR -->>> form is not valid"
            return HttpResponse(msg)
        
#END Admin Register

#User Register
class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'account/usersignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def post(self, request):
        form = self.form_class(request.POST)
        # print(form.cleaned_data)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('login')

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
                        auth.login(request,user)
                        return redirect('admin-profile')
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



class Logout(View):
    def get(self, request):
        auth.logout(request)
        return redirect('home')

