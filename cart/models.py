from django.db import models
from order.models import OrderModel
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Cart(models.Model):
    cart_product_name = models.CharField(max_length=100)    
    cart_product_desc = models.TextField()
    cart_prod_quantity = models.DecimalField(max_digits=1000,decimal_places=0)
    cart_product_price = models.DecimalField(max_digits=1000,decimal_places=2)
    cart_product_discount =  models.FloatField(max_length=4)
    cart_prod_sell_price = models.DecimalField(max_digits=1000,decimal_places=2)
    # cart_prod_net_price =  models.DecimalField(max_digits=1000,decimal_places=2)
    cart_prod_deli_chrg = models.DecimalField(max_digits=1000,decimal_places=2,default=0,null=True)
    # cart_prod_total = models.DecimalField(max_digits=1000,decimal_places=2)
    cart_user_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    order_completed = models.BooleanField(default=False)
    order_number = models.ForeignKey(OrderModel,on_delete=models.DO_NOTHING,null=True)
    product = models.ForeignKey(Product,null=True,blank=True,on_delete=models.DO_NOTHING)


    @property
    def net_price(self):
        NetPrice = self.cart_prod_sell_price * self.cart_prod_quantity
        return NetPrice

    @property
    def net_list_price(self):
        NetListPrice = self.cart_product_price * self.cart_prod_quantity
        return NetListPrice


    

