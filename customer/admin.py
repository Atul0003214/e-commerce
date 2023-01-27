from django.contrib import admin
from .models import CustomerModel,AddressModel

@admin.register(CustomerModel)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','DateOfBirth']

@admin.register(AddressModel)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['customer','Address','Address2','city','state','zip']
