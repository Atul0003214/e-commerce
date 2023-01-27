from django.db import models
from django.contrib.auth.models import User



class OrderModel(models.Model):
    customer = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    completed = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0.0)

    @property
    def order_id(self):
        return 1000+self.id



