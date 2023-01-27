from django.contrib import admin
from .models import OrderModel
# Register your models here.

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','order_id','completed','date_ordered','total']
