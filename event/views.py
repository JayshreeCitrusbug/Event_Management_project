from re import template
from types import MemberDescriptorType
from urllib import request
from django.shortcuts import redirect, render

# Create your views here.
from django.views.generic import View, ListView, DetailView, CreateView
from event.models import Event, Artist, EventBook, Genre, Member , User
from event.forms import UserSignUpForm, UserNewCreationForm
#from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.db import transaction


#Main page
class main(View):
    template_name = "event/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
#method base view of  main      
# def main(request):
#     return render(request, 'event/home.html' , {})


#Event list Detail view
class EventListview(ListView):
    model = Event
    template_name = 'event/event_list.html'

class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event_detail.html'

# END Event list Detail view

#Register/login view
#Admin Register
class UserRegisterView(CreateView):
    model = Member
    form_class = UserNewCreationForm
    template_name = 'account/register.html'
    # success_url = reverse_lazy('login')
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'event_admin'
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, self.template_name)




#User Register
class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'account/usersignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('event-list')






#END Register/login view