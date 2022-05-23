from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Member, Artist, Event, Genre, EventBook
from .forms import AccountUpdateForm, AccountCreationForm
from django.utils.translation import ugettext_lazy as _

# class UserAdmin(UserAdmin):
#     form = AccountUpdateForm
#     add_form = AccountCreationForm

#     list_per_page = 10
#     list_display = ["pk", "email", "username",]

#     fieldsets = (
#         (None, {"fields": ("email", "password")}),
#         (
#             _("Personal info"),
#             {
#                 "fields": (
#                     "first_name",
#                     "last_name",
#                     "username",
#                 )
#             },
#         ),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "groups",
#                     "user_permissions",
#                 )
#             },
#         ),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": (
#                     "first_name",
#                     "last_name",
#                     "email",
#                     "password1",
#                     "password2",
#                 ),
#             },
#         ),
#     )

#     def save_model(self, request, obj, form, change):
#         instance = form.save(commit=False)
#         instance.save()
#         return instance


# class TestimonialAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk"]


# class InquiryAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk"]


# class InquiryTypeAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk"]


# class ShopProductAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk"]


# class ServiceAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk"]


# class ServiceCategoryAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk"]


# class UserPhoneNumberAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk"]


# class PhoneNumberCodeAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk", "code"]


# class ProductCartAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk"]


# class ServiceCartAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk"]


# class PersonalChartAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk"]


# class PurchasedProductAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk"]


# class TransactionDetailAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk"]


# class TimeSlotAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk"]


# class BookedServiceAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk"]


# class NumberCodeAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk", "code", "meaning"]


# class OtherCodeAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk", "code", "meaning"]

# class CategoryImageAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ["pk", "category_image"]


admin.site.register(Member)
admin.site.register(Artist)
admin.site.register(Event)
admin.site.register(Genre)
admin.site.register(EventBook)