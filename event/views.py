from datetime import *
from imaplib import _Authenticator
import json
from re import template
from types import MemberDescriptorType
from urllib import request
from django import forms, views
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views.generic import View, ListView, DetailView, CreateView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from event import forms
from event.models import Event, Artist, EventBook, Genre, Member , User
from django.contrib.auth.models import auth
from django_datatables_too.mixins import DataTableMixin
from django.template.loader import get_template
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from event.mixins import HasPermissionsMixin
from event.forms import  UserNewCreationForm, UserSignUpForm,  AdminLoginForm, AddEventForm,  AddArtistForm, EventBookForm, UserUpdateForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .mixins import HasPermissionsMixin, ModelOptsMixin, SuccessMessageMixin
from .utils import admin_urlname, get_deleted_objects
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# ,  AdminProfileForm, UpdateEventForm,

from django.contrib import messages
# from event.generic import *

#from django.views import generic
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy


MSG_CREATED = '"{}" created successfully.'
MSG_UPDATED = '"{}" updated successfully.'
MSG_DELETED = '"{}" deleted successfully.'
MSG_CANCELED = '"{}" canceled successfully.'

# -.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-..--.-..-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-..--.-..
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

# Price
class Price(View):
    model = Event
    template_name = "event/price.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


#Contact Page    
class Contact(View):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

# -.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-..--.-..-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-..--.-..






        
# -.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-..--.-..-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-..--.-..
# Admin Pannel
# -.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-..--.-..-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-..--.-..        
#Admin Profile View
class AdminProfileView(ListView):
    # un = Member.objects.select_related('user_ptr').all()
    # print('member data' ,un)

    template_name = "account/adminprofile.html"
    context = {}

    def get(self, request):
        #Event data 
        # self.context['showevent'] = Event.objects.all()
        # print('evenrdata',self.context['showevent'])
        # print(type(self.context['showevent']))
   
        # queryset = self.model.objects.getvalues('eventDate')
        mon = []
        count = 0
        self.context['queryset'] = Event.objects.values('eventDate')
        for data in self.context['queryset']:
            for d,v in data.items():
                mon.append(v.month)
                self.context['my_dict'] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
                for i in mon:
                    self.context['my_dict'][i] = mon.count(i)
        print(self.context['my_dict'])

        #User count 
        self.context['total_user_count']= User.objects.all().count() - int(User.objects.filter(is_superuser =True).count())
        print(self.context['total_user_count'],"Total user count")

        self.context['admin_user_count']= Member.objects.all().count()
        print(self.context['admin_user_count'],"Admin user count")
        
        self.context['user_count'] = User.objects.filter(is_staff = False).filter(is_superuser=False).count()
        print(self.context['user_count']," User count")
        return render(request, self.template_name, self.context)
       
        # return render(request,self.template_name,{'showevent':eventData})

# ---------------------------------------------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------------------------------------------
class UserListView(ListView, LoginRequiredMixin,
    PermissionRequiredMixin,
    ModelOptsMixin,
    HasPermissionsMixin,):
    """View for User listing"""

    # paginate_by = 25
    ordering = ["id"]
    model = User
    queryset = model.objects.exclude(is_staff=True)
    template_name = "customadmin/adminuser/user_list.html"
    
    def has_permission(self):

        print('----------------------------is staff------------------------------------')
        print(self.request.user.is_staff)
        print('----------------------------is staff------------------------------------')
        if(self.request.user.is_staff == True):
            return True
        else:
            return super().has_permission()

    def get_queryset(self):
        return self.model.objects.exclude(is_staff=True).exclude(email=self.request.user).exclude(email=None)

    def get_context_data(self, **kwargs):
        """Returns the context data to use in this view."""
        ctx = super().get_context_data(**kwargs)
        if hasattr(self, "model"):
            ctx["opts"] = self.model._meta
        return ctx

class UserDetailView(DetailView, LoginRequiredMixin, PermissionRequiredMixin, ModelOptsMixin):
    template_name = "customadmin/adminuser/user_detail.html"
    context = {}

    def get(self, request, pk):
        self.context['user_detail'] = User.objects.filter(pk=pk).first()
        return render(request, self.template_name, self.context)

class UserCreateView(CreateView,LoginRequiredMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    ModelOptsMixin,
    HasPermissionsMixin):
    """View to create User"""

    model = User
    form_class = UserCreationForm
    template_name = "customadmin/adminuser/user_form.html"
    permission_required = ("customadmin.add_user",)

    def get_form_kwargs(self, **kwargs):
        kwargs = super(UserCreateView, self).get_form_kwargs()
        # kwargs["user"] = self.request.user
        return kwargs


    def get_success_url(self):
        # opts = self.model._meta
        return reverse("customadmin:user-list")


class UserUpdateView(UpdateView, LoginRequiredMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    ModelOptsMixin,
    HasPermissionsMixin):
    """View to update User"""

    model = User
    form_class = UserUpdateForm
    template_name = "customadmin/adminuser/update_user.html"
    permission_required = ("customadmin.change_user",)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # kwargs["user"] = self.request.user
        return kwargs

    def get_success_url(self):
        # opts = self.model._meta
        return reverse("customadmin:user-list")


class UserDeleteView(DeleteView):
    """View to delete User"""

    model = User
    template_name = "customadmin/adminuser/delete_user.html"
    permission_required = ("customadmin.delete_user",)

    # def get_success_message(self):
    #     return MSG_DELETED.format(self.object)

    # def get_success_url(self):
    #     print("MyDeleteView:: get_success_url")
    #     opts = self.model._meta
    #     return reverse(admin_urlname(opts, "list"))

    # def delete(self, request, *args, **kwargs):
    #     """Override delete method."""
    #     response = super().delete(request, *args, **kwargs)
    #     messages.success(self.request, self.get_success_message())
    #     if self.request.is_ajax():
    #         response_data = {}
    #         response_data["result"] = True
    #         response_data["message"] = self.get_success_message()
    #         return JsonResponse(response_data)
    #     return response

    # def get_context_data(self, **kwargs):
    #     """Get deletable objects."""
    #     # Todo: Move to deleted objects mixin and reference self?
    #     ctx = super().get_context_data(**kwargs)
    #     # print(ctx["opts"].__dict__.keys())

    #     # Do some extra work here
    #     opts = self.model._meta

    #     # Populate deleted_objects, a data structure of all related objects that
    #     # will also be deleted.
    #     # deleted_objects, model_count, perms_needed, protected = self.get_deleted_objects([obj], request)
    #     deleted_objects, model_count, protected = get_deleted_objects([self.object])

    #     object_name = str(opts.verbose_name)

    #     # if perms_needed or protected:
    #     if protected:
    #         title = ("Cannot delete %(name)s") % {"name": object_name}
    #     else:
    #         title = ("Are you sure?")

    #     ctx["title"] = title
    #     ctx["deleted_objects"] = deleted_objects
    #     ctx["model_count"] = dict(model_count).items()
    #     ctx["protected"] = protected
    #     return ctx

    # def has_permission(self):

    #     print('----------------------------is staff------------------------------------')
    #     print(self.request.user.is_staff)
    #     print('----------------------------is staff------------------------------------')
    #     if(self.request.user.is_staff == True):
    #         return True
    #     else:
    #         return super().has_permission()

    def get_success_url(self):
        # opts = self.model._meta
        return reverse_lazy("customadmin:user-list")
#END of custom admin user's code .....................................................


# ---------------------------------------------------------------------------------------------------------------
# Event
# ---------------------------------------------------------------------------------------------------------------
class Eventview(ListView):
    model = Event
    template_name = "customadmin/adminuser/event.html"
   

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        """Returns the context data to use in this view."""
        
        ctx = super().get_context_data(**kwargs)
        ctx['showevent'] = Event.objects.all()
        if hasattr(self, "model"):
            ctx["opts"] = self.model._meta
        return ctx

    # context = {}
    # def get(self, request):
    #     #Event data 
    #     self.context['showevent'] = Event.objects.all()
    #     print('eventdata',self.context['showevent'])
    #     return render(request, self.template_name, self.context)

# class EventAdminDetailView(DetailView):
#     template_name = "customadmin/adminuser/event_detail.html"
#     context = {}

#     def get(self, request, pk):
#         self.context['event_detail'] = Event.objects.filter(pk=pk).first()
#         return render(request, self.template_name, self.context)

class AddEventView(CreateView):
    model = Event
    form_class = AddEventForm
    template_name = 'event/add_event.html'

    def post(self, request):
        form =self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form.instance.active = True
            form.save()
            return redirect('customadmin:admin-event-view')
        else:
            msg = "Event can not generated please Try Again "
            return HttpResponse(msg)

class UpdateEventView(UpdateView):
    model = Event
    form_class = AddEventForm
    template_name = 'event/update_event.html'
    

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, {'form':self.form_class})

    def get_success_url(self):
         return reverse_lazy('customadmin:admin-event-view')


class DeleteEventView(DeleteView):
    model = Event
    template_name = 'event/delete_event.html'

    def get_success_url(self):
         return reverse_lazy('customadmin:admin-event-view')


# class EventCount(View):
#     model = Event
#     template_name = 'customadmin/dashboard.html'
#     def get(self, request, *args, **kwargs):
#         # queryset = self.model.objects.getvalues('eventDate')
#         mon = []
#         count = 0
#         queryset = Event.objects.values('eventDate')
#         for data in queryset:
#             for d,v in data.items():
#                 mon.append(v.month)
#                 my_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
#                 for i in mon:
#                     my_dict[i] = mon.count(i)
#         print(my_dict)
#         """# dic = json.dumps(my_dict)
#         # print("DIC", dic)
#         # print(type(dic))
                
#         # print(queryset)"""
#         return render(request, self.template_name, {'my_dict': my_dict})

# ---------------------------------------------------------------------------------------------------------------
# Artist
# ---------------------------------------------------------------------------------------------------------------
class Artistview(ListView):
    model = Artist
    # queryset = model.objects.exclude()
    template_name = "customadmin/adminuser/artist.html"
    
    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        """Returns the context data to use in this view."""
        ctx = super().get_context_data(**kwargs)
        ctx['showartist'] = Artist.objects.all()
        if hasattr(self, "model"):
            ctx["opts"] = self.model._meta
        return ctx
    
    # context = {}
    # def get(self, request):
    #     #Artist data 
    #     self.context['showartist'] = Artist.objects.all()
    #     print('artistdata',self.context['showartist'])
    #     return render(request, self.template_name, self.context)


class AddArtistView(CreateView):
    model = Artist
    form_class = AddArtistForm
    template_name = 'artist/add_artist.html'

    def post(self, request):
        form =self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customadmin:artist-list')
        else:
            msg = "Artist can not generated please Try Again later. "
            return HttpResponse(msg)


class UpdateArtistView(UpdateView):
    model = Artist
    form_class = AddArtistForm
    template_name = 'artist/update_artist.html'
    

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, {'form':self.form_class})

    def get_success_url(self):
         return reverse_lazy('customadmin:admin-artist-view')






# -.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-..--.-..-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-..--.-..
# Normal User Pannel
# -.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-..--.-..-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-..--.-.. 
#User Profile
class Userprofile(ListView):
    model = Event
    template_name = "account/userprofile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


# --------------------------------------------------------------------------
# Event
# --------------------------------------------------------------------------
#Event list/Detail view
class EventListview(ListView):
    model = Event
    template_name = 'event/event_list.html'
    
   
class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event_detail.html'

class EventBookView(View):
    model = EventBook
    template_name = 'event/eventbook.html'
    form_class = EventBookForm
    
    def get(self, request):
        data = EventBook.objects.filter(user=request.user)
        # print("booking data",data)
       
        print(request.user.id)
        # form = self.form.instance.event_id = pk
        # print(form)
        return render(request, self.template_name, {'form':self.form_class,'booking_data':data})

    def post(self,request):
        form =self.form_class(request.POST)
        errors = form.non_field_errors()
        field_errors = [ (field.label, field.errors) for field in form]
        print("field_errors", field_errors)
        print("form",form.is_valid())
        if form.is_valid():
            
            seat = form.cleaned_data.get('seats')
            # select_event = form.changed_data.get('event_id')
            avl_seat = Event.objects.filter('seatAvailable')
            print("seat",seat,"avl_seat",avl_seat)
            if avl_seat>seat:
                avl_seat = avl_seat - seat
                # form.save()
                # form.instance.BookedDate = timezone.now()
                form.save()
                form.instance.user = request.user
                form.save()
                return HttpResponse("Success")
            # return render(request , 'event/success.html')
        else:
            msg = "Can not Book seats Please try again "
            return HttpResponse(msg)



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


# ---------------------------------------------------------------------------------
# Artist
# ---------------------------------------------------------------------------------
#Artist list detail View

class ArtistListview(ListView):
    model = Artist
    template_name = 'artist/artist_list.html'

class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artist/artist_detail.html'

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
            return redirect('customadmin:login')
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
            return redirect('customadmin:login')
        else:
            msg = "ERROR -->>> form is not valid"
            return HttpResponse(msg)

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
                        return redirect('customadmin:admin-profile')
                    else:
                        auth.login(request,user)
                        return render(request,'home.html')
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
        return redirect('customadmin:home')

