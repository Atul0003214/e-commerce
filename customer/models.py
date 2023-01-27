from django.db import models
from django.contrib.auth.models import User
from order.models import OrderModel

class CustomerModel(models.Model):
    user = models.OneToOneField(User,blank=True,on_delete=models.CASCADE,null=True)
    # name = models.CharField(max_length=70,null=True)
    # email = models.EmailField(null=True)
    DateOfBirth = models.DateField() 


    def __str__(self):
        return str(self.user)

class AddressModel(models.Model):
    customer = models.ForeignKey(CustomerModel,on_delete=models.CASCADE)
    order = models.ForeignKey(OrderModel,on_delete=models.SET_NULL,null=True)
    Address = models.CharField(max_length=100,null=True)
    Address2 = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=70,null=True)
    state = models.CharField(max_length=70,null=True)
    zip = models.CharField(max_length=70,null=True)
    fName = models.CharField(max_length=70,null=True)
    lName = models.CharField(max_length=70,null=True)
    current_address = models.BooleanField(default=False)
