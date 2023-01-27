from django.contrib import admin
from .models import Cart

# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_product_name','cart_product_desc','cart_prod_quantity','cart_product_price','cart_user_id','net_price']
