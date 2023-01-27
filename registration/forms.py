from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from customer.models import CustomerModel
from django import forms

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ('first_name','last_name','email','username','DateOfBirth')
        fields = ('first_name','last_name','email','username')

class createUserFormCustome(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = ('DateOfBirth',)
        




